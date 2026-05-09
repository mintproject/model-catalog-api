import { describe, it, expect } from 'vitest';
import {
  MAX_DEPTH,
  MAX_NODES,
  MAX_ARRAY_LENGTH,
  ValidationError,
  type WriteNode,
  type JunctionEdge,
  type ChildFkEdge,
} from '../nested-tree.js';
import { buildTree } from '../nested-tree.js';
import { getResourceConfig } from '../resource-registry.js';

describe('nested-tree types and constants', () => {
  it('exposes hard caps as numeric constants', () => {
    expect(MAX_DEPTH).toBe(8);
    expect(MAX_NODES).toBe(500);
    expect(MAX_ARRAY_LENGTH).toBe(200);
  });

  it('ValidationError carries code, path, message, http status', () => {
    const err = new ValidationError('DEPTH_EXCEEDED', '/hasVersion/0', 'too deep', 400);
    expect(err.code).toBe('DEPTH_EXCEEDED');
    expect(err.path).toBe('/hasVersion/0');
    expect(err.message).toBe('too deep');
    expect(err.httpStatus).toBe(400);
    expect(err).toBeInstanceOf(Error);
  });

  it('WriteNode/JunctionEdge/ChildFkEdge can be constructed', () => {
    const node: WriteNode = {
      table: 'modelcatalog_software',
      id: 'https://w3id.org/okn/i/mint/x',
      columns: { label: 'foo' },
      junctions: [],
      childFks: [],
    };
    const junc: JunctionEdge = {
      apiFieldName: 'hasInput',
      junctionTable: 'modelcatalog_configuration_input',
      junctionRelName: 'input',
      parentFkColumn: 'configuration_id',
      targetFkColumn: 'input_id',
      junctionColumns: [],
      children: [],
    };
    const child: ChildFkEdge = {
      apiFieldName: 'hasConfiguration',
      childTable: 'modelcatalog_model_configuration',
      childFkColumn: 'model_version_id',
      children: [],
    };
    expect(node.id).toBe('https://w3id.org/okn/i/mint/x');
    expect(junc.targetFkColumn).toBe('input_id');
    expect(child.childFkColumn).toBe('model_version_id');
  });
});

describe('buildTree — single-level junction', () => {
  it('builds tree for ModelConfiguration with hasInput id-only payload', () => {
    const cfg = getResourceConfig('modelconfigurations')!;
    const body = {
      id: 'cfg-1',
      label: 'my config',
      hasInput: [{ id: 'ds-existing-1' }],
    };

    const tree = buildTree(body, cfg);

    expect(tree.table).toBe('modelcatalog_configuration');
    expect(tree.id).toBe('https://w3id.org/okn/i/mint/cfg-1');
    expect(tree.columns).toEqual({ label: 'my config' });
    expect(tree.junctions).toHaveLength(1);

    const j = tree.junctions[0];
    expect(j.apiFieldName).toBe('hasInput');
    expect(j.junctionTable).toBe('modelcatalog_configuration_input');
    expect(j.junctionRelName).toBe('input');
    expect(j.parentFkColumn).toBe('configuration_id');
    expect(j.targetFkColumn).toBe('input_id');
    expect(j.children).toHaveLength(1);
    expect(j.children[0].id).toBe('https://w3id.org/okn/i/mint/ds-existing-1');
    expect(j.children[0].columns).toEqual({});
    expect(j.children[0].table).toBe('modelcatalog_dataset_specification');
  });

  it('captures scalar fields on nested target entity (upsert path)', () => {
    const cfg = getResourceConfig('modelconfigurations')!;
    const body = {
      id: 'cfg-2',
      hasInput: [{ id: 'ds-2', label: 'updated label' }],
    };
    const tree = buildTree(body, cfg);
    expect(tree.junctions[0].children[0].columns).toEqual({ label: 'updated label' });
  });

  it('captures junction extra columns (is_optional)', () => {
    const cfg = getResourceConfig('modelconfigurations')!;
    const body = {
      id: 'cfg-3',
      hasInput: [{ id: 'ds-3', isOptional: true }],
    };
    const tree = buildTree(body, cfg);
    expect(tree.junctions[0].junctionColumns).toEqual([{ is_optional: true }]);
    expect(tree.junctions[0].children[0].columns).toEqual({});
  });

  it('auto-generates id when nested entity lacks one', () => {
    const cfg = getResourceConfig('modelconfigurations')!;
    const body = {
      id: 'cfg-4',
      hasInput: [{ label: 'brand new ds' }],
    };
    const tree = buildTree(body, cfg);
    expect(tree.junctions[0].children[0].id).toMatch(/^https:\/\/w3id\.org\/okn\/i\/mint\/[0-9a-f-]{36}$/);
  });
});

describe('buildTree — recursion (multi-level)', () => {
  it('walks 2 levels: ModelConfiguration > hasInput > hasPresentation', () => {
    const cfg = getResourceConfig('modelconfigurations')!;
    const body = {
      id: 'cfg-deep',
      hasInput: [
        {
          id: 'ds-deep',
          label: 'deep ds',
          hasPresentation: [{ id: 'vp-1', label: 'pres' }],
        },
      ],
    };
    const tree = buildTree(body, cfg);
    const ds = tree.junctions[0].children[0];
    expect(ds.id).toBe('https://w3id.org/okn/i/mint/ds-deep');
    expect(ds.columns).toEqual({ label: 'deep ds' });
    expect(ds.junctions.length).toBeGreaterThanOrEqual(1);
    const pres = ds.junctions.find((j) => j.apiFieldName === 'hasPresentation');
    expect(pres).toBeDefined();
    expect(pres!.children[0].id).toBe('https://w3id.org/okn/i/mint/vp-1');
    expect(pres!.children[0].columns).toEqual({ label: 'pres' });
  });
});
