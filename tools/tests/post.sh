DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source $DIR/env

#POST
echo "Inserting the model"
payload=$(cat input.json)
MODEL=$(curl -X POST "$SERVER/modelconfigurations" -H "Authorization: Bearer $TOKEN" -H "accept: */*" -H "Content-Type: application/json" -d "$payload")
MODEL_ID=$(echo $MODEL | jq -r '.id')
echo "ID model is: $MODEL_ID"
echo "Obtain the model"
curl -X GET "$SERVER/modelconfigurations/$MODEL_ID?username=mint@isi.edu" -H "accept: application/json" | jq -r "."
