DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source $DIR/env

TOKEN=$(curl -s -X GET "http://localhost:8080/v1.0.0/user/login?username=mint%40isi.edu&password=mint123" -H "accept: application/json" | jq -r '.access_token')
#GET
curl -s -X GET "http://localhost:8080/v1.0.0/models?username=mint@isi.edu" -H "accept: application/json" | jq -r "."