set -xe
mkdir -p ~/.openapi-generator/templates/ && cd $_
curl -L https://api.github.com/repos/OpenAPITools/openapi-generator/tarball | tar xz
pwd
mv ./modules/openapi-generator/src/main/resources/python-flask ./python-flask
rm -rf OpenAPITools-openapi-generator-*
