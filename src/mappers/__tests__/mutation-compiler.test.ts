import { describe, it, expect } from 'vitest';
import { compilePost } from '../mutation-compiler.js';
import type { WriteNode } from '../nested-tree.js';

describe('compilePost', () => {
  it('emits scalar-only insert when no relationships', () => {
    const tree: WriteNode = {
      table: 'modelcatalog_software',
      id: 'https://w3id.org/okn/i/mint/sw-1',
      columns: { label: 'foo' },
      junctions: [],
      childFks: [],
    };
    const { mutation, variables } = compilePost(tree);
    expect(mutation).toMatch(/insert_modelcatalog_software_one/);
    expect(mutation).toMatch(/object: \$object/);
    expect(variables).toEqual({
      object: { id: 'https://w3id.org/okn/i/mint/sw-1', label: 'foo' },
    });
  });

  it('emits nested junction insert with dynamic update_columns from columns keys', () => {
    const tree: WriteNode = {
      table: 'modelcatalog_configuration',
      id: 'cfg-1',
      columns: { label: 'cfg' },
      junctions: [
        {
          apiFieldName: 'hasInput',
          junctionTable: 'modelcatalog_configuration_input',
          junctionRelName: 'input',
          parentFkColumn: 'configuration_id',
          targetFkColumn: 'input_id',
          junctionColumns: [{}],
          children: [
            {
              table: 'modelcatalog_dataset_specification',
              id: 'ds-1',
              columns: { label: 'ds-label' },
              junctions: [],
              childFks: [],
            },
          ],
        },
      ],
      childFks: [],
    };
    const { variables } = compilePost(tree);
    const obj = (variables.object as Record<string, unknown>);
    expect(obj.id).toBe('cfg-1');
    expect(obj.label).toBe('cfg');
    const inputs = (obj.input as { data: unknown[]; on_conflict: { update_columns: string[] } });
    expect(inputs.on_conflict.update_columns).toEqual([]);
    const inputRow = inputs.data[0] as Record<string, any>;
    const nested = inputRow.input as { data: any; on_conflict: { update_columns: string[] } };
    expect(nested.data.id).toBe('ds-1');
    expect(nested.data.label).toBe('ds-label');
    expect(nested.on_conflict.update_columns).toEqual(['label']);
    expect(nested.on_conflict.constraint).toBe('modelcatalog_dataset_specification_pkey');
  });

  it('emits link-only nested entity (empty columns) with update_columns:[]', () => {
    const tree: WriteNode = {
      table: 'modelcatalog_configuration',
      id: 'cfg-2',
      columns: {},
      junctions: [
        {
          apiFieldName: 'hasInput',
          junctionTable: 'modelcatalog_configuration_input',
          junctionRelName: 'input',
          parentFkColumn: 'configuration_id',
          targetFkColumn: 'input_id',
          junctionColumns: [{}],
          children: [
            {
              table: 'modelcatalog_dataset_specification',
              id: 'ds-existing',
              columns: {},
              junctions: [],
              childFks: [],
            },
          ],
        },
      ],
      childFks: [],
    };
    const { variables } = compilePost(tree);
    const obj = variables.object as Record<string, any>;
    const nested = (obj.input.data[0].input) as { on_conflict: { update_columns: string[] } };
    expect(nested.on_conflict.update_columns).toEqual([]);
  });

  it('applies junction extra columns to junction row', () => {
    const tree: WriteNode = {
      table: 'modelcatalog_configuration',
      id: 'cfg-3',
      columns: {},
      junctions: [
        {
          apiFieldName: 'hasInput',
          junctionTable: 'modelcatalog_configuration_input',
          junctionRelName: 'input',
          parentFkColumn: 'configuration_id',
          targetFkColumn: 'input_id',
          junctionColumns: [{ is_optional: true }],
          children: [
            { table: 'modelcatalog_dataset_specification', id: 'ds', columns: {}, junctions: [], childFks: [] },
          ],
        },
      ],
      childFks: [],
    };
    const { variables } = compilePost(tree);
    const row = (variables.object as any).input.data[0];
    expect(row.is_optional).toBe(true);
  });

  it('emits childFk nested-array insert with FK column set on each child', () => {
    const tree: WriteNode = {
      table: 'modelcatalog_software_version',
      id: 'sv-1',
      columns: { label: 'v' },
      junctions: [],
      childFks: [
        {
          apiFieldName: 'hasConfiguration',
          childTable: 'modelcatalog_model_configuration',
          childFkColumn: 'software_version_id',
          children: [
            { table: 'modelcatalog_model_configuration', id: 'cfg-a', columns: { label: 'A' }, junctions: [], childFks: [] },
            { table: 'modelcatalog_model_configuration', id: 'cfg-b', columns: {}, junctions: [], childFks: [] },
          ],
        },
      ],
    };
    const { variables } = compilePost(tree);
    const obj = variables.object as any;
    expect(obj.model_configurations).toBeDefined();
    const childKey = Object.keys(obj).find((k) => k !== 'id' && k !== 'label')!;
    const arr = obj[childKey].data as any[];
    expect(arr.length).toBe(2);
    expect(arr[0].software_version_id).toBe('sv-1');
    expect(arr[0].id).toBe('cfg-a');
    expect(arr[0].label).toBe('A');
    expect(arr[1].software_version_id).toBe('sv-1');
  });
});
