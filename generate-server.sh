#!/usr/bin/env bash
dir=${PWD}
rm -rf server-v1.0.0
docker run -ti --rm -v ${PWD}:/local openapitools/openapi-generator-cli:v4.1.2 \
     generate  \
     -i /local/model-catalog-v1.0.0.yaml\
     -g python-flask  \
     -o /local/server-v1.0.0/ \
     --git-repo-id MINT-ModelCatalogIngestionAPI \
     --git-user-id mintproject \
     --template-dir /local/.openapi-generator/template \
     --ignore-file-override /local/.openapi-generator-ignore
rm -f server-v1.0.0/openapi_server/controllers/default_controller.py
cp -rv ${PWD}/.openapi-generator/template/static_files/utils/ ${PWD}/server-v1.0.0/openapi_server/utils/
cp -rv ${PWD}/.openapi-generator/template/static_files/settings/ ${PWD}/server-v1.0.0/openapi_server/settings/
cp -rv ${PWD}/.openapi-generator/template/static_files/user_controller.py ${PWD}/server-v1.0.0/openapi_server/controllers/
cp -rv ${PWD}/.openapi-generator/template/static_files/contexts/ ${PWD}/server-v1.0.0/contexts/
cp -rv ${PWD}/.openapi-generator/template/static_files/queries/ ${PWD}/server-v1.0.0/queries/
