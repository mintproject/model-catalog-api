rsync --delete -av ~/ISI/model-catalog-oas/model-catalog/servers/python/server/ server

git checkout -- server/.env \
    server/docker-compose.yml \
    server/openapi_server/settings/config.ini \
    server/openapi_server/test/ \
    server/openapi_server/test/input_tests/model_configuration_without_id.json \
    server/openapi_server/test/input_tests/model_configuration_without_id_causal_diagram_not_equal.json \
    server/openapi_server/cached.py \
    server/openapi_server/__main__.py \
    server/contexts/context_overwrite.json \
    server/requirements.txt \
    server/git_push.sh

rm -rf server/openapi_server/controllers/default_controller.py server/.travis.yml server/.gitignore server/queries/queries/

rsync --delete -av ~/ISI/model-catalog-oas/model-catalog/servers/python/openapi.yaml openapi.yaml

swagger-cli bundle -o server/openapi.json openapi.yaml

pushd server/openapi_server/models
sed -i.bak 's/AnyOf[a-zA-Z]*/object/g' *.py
sed -i.bak '/from openapi_server.models.any/d' *.py
for file in $(ls *.bak); do
    rm $file
done
