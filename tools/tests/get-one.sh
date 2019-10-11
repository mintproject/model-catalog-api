DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source $DIR/env
#GET
curl -s -X GET "$SERVER/modelconfigurations/$1?username=mint@isi.edu" -H "accept: application/json" | jq -r "."



DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source $DIR/env

if [ "$#" -ne 2 ] ; then
    echo "Illegal number of parameters"
    echo "bash get-one.sh datasetspecifications pihm_geol"
    exit 1
fi
CLASS=$1
ID=$2
echo "Get one resources $ID $CLASS"

curl -X GET "$SERVER/$CLASS/$ID?username=mint@isi.edu" -H "accept: application/json" | jq -r "." | tee resources/$ID.json