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
