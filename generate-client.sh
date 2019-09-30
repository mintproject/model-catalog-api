#!/usr/bin/env bash
dir=${PWD}
rm -rf server-v1.0.0
docker run -ti --rm -v ${PWD}:/local openapitools/openapi-generator-cli:v4.1.2 \
     generate  \
     -i /local/model-catalog-v1.0.0.yaml\
     -g typescript-fetch \
     -o /local/client-v1.0.0/ \
     --git-repo-id model-catalog-client \
     --git-user-id mintproject \
     --ignore-file-override /local/.openapi-generator-ignore

