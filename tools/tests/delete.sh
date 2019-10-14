DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source $DIR/env

if [ "$#" -ne 2 ] ; then
    echo "Illegal number of parameters"
    echo "bash delete.sh datasetspecifications cycles_crop.json"
    exit 1
fi
CLASS=$1
ID=$2
echo "Deleting $CLASS $ID"
curl -X DELETE "$SERVER/$CLASS/$ID" -H "Authorization: Bearer $TOKEN" -H "accept: */*" -H "Content-Type: application/json"
