DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source $DIR/env
#POST
echo "Inserting the model"
curl -X POST "$SERVER/v1.0.0/persons?username=mint@isi.edu" -H "accept: */*" -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d "{\"email\":[\"some@mail.com\"],\"label\":\"Person 1\"}" -v

