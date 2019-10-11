DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source $DIR/env

if [ "$#" -ne 3 ] ; then
    echo "Illegal number of parameters"
    echo "bash put.sh datasetspecifications cycles_crop cycles_crop.json"
    exit 1
fi
CLASS=$1
ID=$2
FILE=$3
echo "Updating the model: $ID, using $FILE"

#PUT
payload=$(cat $FILE)
curl -X PUT "$SERVER/$CLASS/$ID" -H "Authorization: Bearer $TOKEN" -H "accept: */*" -H "Content-Type: application/json" -d "$payload"
