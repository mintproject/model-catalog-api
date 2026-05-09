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

describe('nested-write e2e — softwares.hasVersion (bug-089 class)', () => {
  // Expected: PASS once bug-089 implementation lands. May FAIL on this branch today.
  it('POST software with an inline nested hasVersion creates the version row and links it via FK', async () => {
    const softwareId = uniqueId('software');
    const versionId = uniqueId('softwareversion');

    const res = await inject(app, 'POST', '/v2.0.0/softwares', {
      id: softwareId,
      label: ['sw-nested'],
      type: ['Software'],
      hasVersion: [
        { id: versionId, label: ['v-nested'], type: ['SoftwareVersion'] },
      ],
    });
    expect(res.statusCode).toBeGreaterThanOrEqual(200);
    expect(res.statusCode).toBeLessThan(300);
    trackId('softwares', softwareId);
    trackId('softwareversions', versionId);

    const swGet = await inject(
      app, 'GET',
      `/v2.0.0/softwares/${encodeURIComponent(softwareId)}`,
    );
    const sw = (Array.isArray(swGet.body) ? swGet.body[0] : swGet.body) as {
      hasVersion?: { id: string }[];
    };
    expect(sw.hasVersion?.map((v) => v.id)).toContain(versionId);

    const verGet = await inject(
      app, 'GET',
      `/v2.0.0/softwareversions/${encodeURIComponent(versionId)}`,
    );
    expect(verGet.statusCode).toBe(200);
    const ver = (Array.isArray(verGet.body) ? verGet.body[0] : verGet.body) as {
      id: string; label: string[];
    };
    expect(ver.id).toBe(versionId);
    expect(ver.label).toEqual(['v-nested']);
  });
});
