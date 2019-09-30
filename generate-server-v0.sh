#!/usr/bin/env bash
dir=${PWD}

docker run -ti --rm -v ${PWD}:/local openapitools/openapi-generator-cli:v4.0.0 \
     generate  \
     -i /local/model-catalog-v0.0.2.yaml\
     -g python-flask  \
     -o /local/server-v0.0.2/ \
     --git-repo-id MINT-ModelCatalogIngestionAPI \
     --git-user-id mintproject \
     --template-dir /local/.openapi-generator-v0/template \
     --ignore-file-override /local/.openapi-generator-ignore
