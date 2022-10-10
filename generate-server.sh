#!/usr/bin/env bash
set -e
dir=${PWD}

copy_static_files=true
echo "Generating server"
while getopts 'ibc:h' opt; do
    case "$opt" in
    i)
        echo "The static files will not be copied"
        copy_static_files=false
        ;;

    ? | h)
        echo "Usage: $(basename $0) [-a] [-b] [-c arg]"
        exit 1
        ;;
    esac
done
shift "$(($OPTIND - 1))"

SERVER_DIR=server
docker run -ti --rm -v ${PWD}:/local openapitools/openapi-generator-cli:v4.1.2 \
    generate \
    -i /local/model-catalog.yaml -g python-flask \
    -o /local/$SERVER_DIR/ \
    --git-repo-id model-catalog-api \
    --git-user-id mintproject \
    --template-dir /local/.openapi-generator/template \
    --ignore-file-override /local/.openapi-generator-ignore
rm -f $SERVER_DIR/openapi_server/controllers/default_controller.py

if [ "$copy_static_files" = true ]; then
    echo "Copying static files"
    cp -rv ${PWD}/.openapi-generator/template/static_files/utils/ ${PWD}/$SERVER_DIR/openapi_server/
    cp -rv ${PWD}/.openapi-generator/template/static_files/settings/ ${PWD}/$SERVER_DIR/openapi_server/
    cp -rv ${PWD}/.openapi-generator/template/static_files/user_controller.py ${PWD}/$SERVER_DIR/openapi_server/controllers/
    cp -rv ${PWD}/.openapi-generator/template/static_files/contexts/ ${PWD}/$SERVER_DIR/
    cp -rv ${PWD}/.openapi-generator/template/static_files/queries/ ${PWD}/$SERVER_DIR/
else
    echo "Skipping static files"
fi

pushd server/openapi_server/models
sed -i.bak 's/AnyOf[a-zA-Z]*/object/g' *.py
sed -i.bak '/from openapi_server.models.any/d' *.py
for file in $(ls *.bak); do
    rm $file
done
popd
