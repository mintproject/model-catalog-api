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
