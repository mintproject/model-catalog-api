/**
 * Two-pass nested write pipeline — Pass 1.
 *
 * buildTree() (added in Task 2) walks the request body via resource-registry,
 * normalizes payload, validates caps/cycles/string-ids, assigns ids, and
 * returns a WriteTree consumed by mutation-compiler.ts.
 */

export const MAX_DEPTH = 8;
export const MAX_NODES = 500;
export const MAX_ARRAY_LENGTH = 200;

export type ValidationCode =
  | 'DEPTH_EXCEEDED'
  | 'TOO_MANY_NODES'
  | 'ARRAY_TOO_LONG'
  | 'CYCLE'
  | 'STRING_ID_DEPRECATED'
  | 'UNKNOWN_FIELD'
  | 'TARGET_NOT_IMPLEMENTED';

export class ValidationError extends Error {
  constructor(
    public readonly code: ValidationCode,
    public readonly path: string,
    message: string,
    public readonly httpStatus: number,
  ) {
    super(message);
    this.name = 'ValidationError';
  }
}

export interface WriteNode {
  table: string;
  id: string;
  columns: Record<string, unknown>;
  junctions: JunctionEdge[];
  childFks: ChildFkEdge[];
  apiType?: string;
}

export interface JunctionEdge {
  apiFieldName: string;
  junctionTable: string;
  junctionRelName: string;
  parentFkColumn: string;
  targetFkColumn: string;
  junctionColumns: Record<string, unknown>[];
  children: WriteNode[];
}

export interface ChildFkEdge {
  apiFieldName: string;
  childTable: string;
  childFkColumn: string;
  children: WriteNode[];
}
