dir=${PWD}
parentdir="$(dirname "$dir")"

docker run -ti --rm -v ${PWD}:/local openapitools/openapi-generator-cli \
     generate  \
     -i /local/model-catalog-v0.0.2.yaml\
     -g python-flask  \
     -o /local/server/ \
     --git-repo-id MINT-ModelCatalogIngestionAPI
     --git-user-id mintproject 
