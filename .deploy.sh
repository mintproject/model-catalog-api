#!/bin/bash
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker tag model-catalog-api mintproject/model-catalog-api:$TRAVIS_TAG
docker push -f mintproject/model-catalog-api:$TRAVIS_TAG

git clone https://github.com/mintproject/model-catalog-python-api-client.git
pushd model-catalog-python-api-client
bash generate-client.sh $TRAVIS_TAG
release-it --config .release-it.json --ci
popd

git clone https://github.com/mintproject/model-catalog-fetch-api-client.git
pushd model-catalog-fetch-api-client
bash generate-client.sh $TRAVIS_TAG
echo "//registry.npmjs.org/:_authToken=$NPM_TOKEN" > .npmrc
release-it --config .release-it.json --ci
