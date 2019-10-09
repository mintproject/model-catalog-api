DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source $DIR/env

if [ "$#" -ne 1 ]; then
    echo "Illegal number of parameters"
    echo "bash put.sh ID"
    exit 1
fi
MODEL_ID=$1
echo "Updating the model: $MODEL_ID"

#PUT
payload=$(cat input.json)
MODEL=$(curl -X PUT "$SERVER/v1.0.0/modelconfigurations/$MODEL_ID" -H "Authorization: Bearer $TOKEN" -H "accept: */*" -H "Content-Type: application/json" -d "$payload")
curl -X GET "$SERVER/v1.0.0/modelconfigurations/$MODEL_ID?username=mint@isi.edu" -H "accept: application/json" |  jq -r "."
