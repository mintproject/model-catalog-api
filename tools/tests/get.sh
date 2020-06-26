DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source $DIR/env

if [ "$#" -ne 1 ] ; then
    echo "Illegal number of parameters"
    echo "bash get.sh datasetspecifications"
    exit 1
fi
CLASS=$1
curl -s -X GET "$SERVER/$CLASS?username=$USERNAME" -H "accept: application/json" | jq -r ".[].id"
