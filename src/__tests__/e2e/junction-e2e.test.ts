import { describe, it, expect, beforeAll, afterAll } from 'vitest';
import type { FastifyInstance } from 'fastify';
import { assertHasuraReachable, buildE2EApp } from './setup.js';
import { cleanup, inject, trackId, uniqueId } from './helpers.js';

let app: FastifyInstance;
beforeAll(async () => {
  await assertHasuraReachable();
  app = await buildE2EApp();
});
afterAll(async () => {
  if (app) {
    await cleanup(app);
    await app.close();
  }
});

describe('junction e2e — softwareversions.hasGrid (bug-087 class)', () => {
  it('does NOT clobber an existing grid label when linked from a new softwareversion (bug-087 regression)', async () => {
    // 1. Create a grid with a known label.
    const gridId = uniqueId('grid');
    const ORIGINAL_LABEL = 'original-grid-label-DO-NOT-CLOBBER';
    const gridCreate = await inject(app, 'POST', '/v2.0.0/grids', {
      id: gridId,
      label: [ORIGINAL_LABEL],
      type: ['Grid'],
    });
    expect(gridCreate.statusCode).toBeGreaterThanOrEqual(200);
    expect(gridCreate.statusCode).toBeLessThan(300);
    trackId('grids', gridId);

    // 2. Create a softwareversion linking to that grid by ID only (no label in the link payload).
    const versionId = uniqueId('softwareversion');
    const versionCreate = await inject(app, 'POST', '/v2.0.0/softwareversions', {
      id: versionId,
      label: ['e2e-version'],
      type: ['SoftwareVersion'],
      hasGrid: [{ id: gridId }],
    });
    expect(versionCreate.statusCode).toBeGreaterThanOrEqual(200);
    expect(versionCreate.statusCode).toBeLessThan(300);
    trackId('softwareversions', versionId);

    // 3. Fetch the grid back and assert its label was NOT touched.
    const gridGet = await inject(
      app,
      'GET',
      `/v2.0.0/grids/${encodeURIComponent(gridId)}`,
    );
    expect(gridGet.statusCode).toBe(200);
    const grid = (Array.isArray(gridGet.body) ? gridGet.body[0] : gridGet.body) as {
      id: string;
      label: string[];
    };
    expect(grid.id).toBe(gridId);
    expect(grid.label).toEqual([ORIGINAL_LABEL]);
  });
});
