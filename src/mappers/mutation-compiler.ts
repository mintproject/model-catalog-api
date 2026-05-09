/**
 * Two-pass nested write pipeline — Pass 2.
 *
 * compilePost() takes a WriteNode tree (from buildTree / Pass 1) and compiles
 * it into a Hasura insert mutation string + variables object ready for Apollo.
 */

import type { WriteNode, JunctionEdge, ChildFkEdge } from './nested-tree.js';

export interface CompiledMutation {
  mutation: string;
  variables: Record<string, unknown>;
}

function tableSuffix(table: string): string {
  return table.replace('modelcatalog_', '');
}

function buildInsertObject(node: WriteNode): Record<string, unknown> {
  const obj: Record<string, unknown> = { id: node.id, ...node.columns };

  for (const j of node.junctions) {
    obj[j.junctionRelName] = buildJunctionInsert(j);
  }
  for (const c of node.childFks) {
    obj[childFkRelKey(c)] = buildChildFkInsert(c);
  }
  return obj;
}

function buildJunctionInsert(j: JunctionEdge): Record<string, unknown> {
  const data = j.children.map((child, idx) => {
    const row: Record<string, unknown> = {
      ...j.junctionColumns[idx],
      [j.junctionRelName]: {
        data: buildInsertObject(child),
        on_conflict: {
          constraint: `${child.table}_pkey`,
          update_columns: Object.keys(child.columns),
        },
      },
    };
    return row;
  });
  return {
    data,
    on_conflict: {
      constraint: `${j.junctionTable}_pkey`,
      update_columns: [],
    },
  };
}

function buildChildFkInsert(c: ChildFkEdge): Record<string, unknown> {
  const data = c.children.map((child) => buildInsertObject(child));
  return {
    data,
    on_conflict: {
      constraint: `${c.childTable}_pkey`,
      update_columns: c.children.flatMap((ch) => Object.keys(ch.columns)),
    },
  };
}

function childFkRelKey(c: ChildFkEdge): string {
  return tableSuffix(c.childTable) + 's';
}

function buildPutJunctionRow(j: JunctionEdge, idx: number): Record<string, unknown> {
  const child = j.children[idx];
  const row: Record<string, unknown> = { ...j.junctionColumns[idx] };
  row[j.junctionRelName] = {
    data: buildInsertObject(child),
    on_conflict: {
      constraint: `${child.table}_pkey`,
      update_columns: Object.keys(child.columns),
    },
  };
  return row;
}

export function compilePut(tree: WriteNode): CompiledMutation {
  const suffix = tableSuffix(tree.table);
  const variables: Record<string, unknown> = { id: tree.id, set: tree.columns };
  const parts: string[] = [
    `update_modelcatalog_${suffix}_by_pk(pk_columns: { id: $id }, _set: $set) { id }`,
  ];
  const varDecls: string[] = [`$id: String!`, `$set: modelcatalog_${suffix}_set_input!`];

  for (const j of tree.junctions) {
    const juncSuffix = tableSuffix(j.junctionTable);
    parts.push(
      `del_${j.junctionRelName}s: delete_modelcatalog_${juncSuffix}(where: { ${j.parentFkColumn}: { _eq: $id } }) { affected_rows }`,
    );
    if (j.children.length > 0) {
      const varName = `junc_${j.junctionRelName}s`;
      const objects = j.children.map((_, i) => buildPutJunctionRow(j, i));
      variables[varName] = objects;
      varDecls.push(`$${varName}: [modelcatalog_${juncSuffix}_insert_input!]!`);
      parts.push(
        `ins_${j.junctionRelName}s: insert_modelcatalog_${juncSuffix}(objects: $${varName}, on_conflict: { constraint: modelcatalog_${juncSuffix}_pkey, update_columns: [] }) { affected_rows }`,
      );
    }
  }

  for (const c of tree.childFks) {
    const childSuffix = tableSuffix(c.childTable);
    const childSuffixPlural = `${childSuffix}s`;
    const idsVar = `child_ids_${childSuffixPlural}`;
    const objsVar = `child_${childSuffixPlural}`;
    const ids = c.children.map((ch) => ch.id);
    const objects = c.children.map((ch) => ({ ...buildInsertObject(ch), [c.childFkColumn]: tree.id }));
    variables[idsVar] = ids;
    variables[objsVar] = objects;
    varDecls.push(`$${idsVar}: [String!]!`);
    varDecls.push(`$${objsVar}: [modelcatalog_${childSuffix}_insert_input!]!`);
    const updateCols = c.children.flatMap((ch) => Object.keys(ch.columns));
    const updateColsStr = updateCols.length > 0 ? updateCols.join(', ') : '';
    parts.push(
      `clear_${childSuffixPlural}: update_modelcatalog_${childSuffix}(where: { ${c.childFkColumn}: { _eq: $id }, id: { _in: $${idsVar} } }, _set: { ${c.childFkColumn}: null }) { affected_rows }`,
    );
    parts.push(
      `upsert_${childSuffixPlural}: insert_modelcatalog_${childSuffix}(objects: $${objsVar}, on_conflict: { constraint: modelcatalog_${childSuffix}_pkey, update_columns: [${updateColsStr}] }) { affected_rows }`,
    );
  }

  const mutation = `
    mutation UpdateMutation(${varDecls.join(', ')}) {
      ${parts.join('\n      ')}
    }
  `;
  return { mutation, variables };
}

export function compilePost(tree: WriteNode): CompiledMutation {
  const object = buildInsertObject(tree);

  // Inject FK column values into childFk rows after the object is built
  for (const c of tree.childFks) {
    const arr = (object[childFkRelKey(c)] as { data: Record<string, unknown>[] }).data;
    arr.forEach((row, idx) => {
      row[c.childFkColumn] = tree.id;
      const childNode = c.children[idx];
      for (const subC of childNode.childFks) {
        const subArr = (row[childFkRelKey(subC)] as { data: Record<string, unknown>[] }).data;
        subArr.forEach((subRow) => {
          subRow[subC.childFkColumn] = childNode.id;
        });
      }
    });
  }

  const suffix = tableSuffix(tree.table);
  const mutation = `
    mutation CreateMutation($object: modelcatalog_${suffix}_insert_input!) {
      insert_modelcatalog_${suffix}_one(object: $object) { id }
    }
  `;
  return { mutation, variables: { object } };
}
