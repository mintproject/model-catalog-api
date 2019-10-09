DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source $DIR/env
#GET
curl -s -X GET "$SERVER/v1.0.0/modelconfigurations/$1?username=mint@isi.edu" -H "accept: application/json" | jq -r "."
