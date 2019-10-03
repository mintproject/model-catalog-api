DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source $DIR/env

if [ "$#" -ne 1 ]; then
    echo "Illegal number of parameters"
    echo "bash delete.sh ID"
    exit 1
fi
MODEL_ID=$1

TOKEN=$(curl -s -X GET "$SERVER/v1.0.0/user/login?username=mint%40isi.edu&password=mint123" -H "accept: application/json" | jq -r '.access_token')
echo "Obtaining the model: $MODEL_ID"
curl -X GET "$SERVER/v1.0.0/models/$MODEL_ID?username=mint@isi.edu" -H "accept: application/json" | jq -r "."
echo "Deleting the model: $MODEL_ID"
curl -X DELETE -H "Authorization: Bearer $TOKEN" "$SERVER/v1.0.0/models/$MODEL_ID" -H "accept: application/json"
curl -X GET "$SERVER/v1.0.0/models/$MODEL_ID?username=mint@isi.edu" -H "accept: application/json" | jq -r "."
