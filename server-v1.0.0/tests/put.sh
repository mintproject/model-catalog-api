DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source $DIR/env

if [ "$#" -ne 1 ]; then
    echo "Illegal number of parameters"
    echo "bash put.sh ID"
    exit 1
fi
MODEL_ID=$1
echo "Updating the model: $MODEL_ID"

#POST
MODEL=$(curl -s -X PUT "$SERVER/v1.0.0/models/$MODEL_ID" -H "Authorization: Bearer $TOKEN" -H "accept: */*" -H "Content-Type: application/json" -d "{\"description\":[\"Decision Support System for Agrotechnology Transfer (DSSAT) is software application program that comprises dynamic crop growth simulation models for over 40 crops. DSSAT is supported by a range of utilities and applications for weather; soil; genetic; crop management and observational experimental data. Includes example data sets for all crop models. The crop simulation models simulate growth; development and yield as a function of the soil-plant-atmosphere dynamics\"],\"hasDocumentation\":[\"https://dssat.net\"],\"hasModelCategory\":[\"Agriculture\"],\"hasVersion\":[{\"id\":\"DSSAT_4.7\"}],\"id\":\"DSSAT\",\"label\":\"Decision Support System for Agrotechnology Transfer (DSSAT)\",\"type\":[\"https://w3id.org/okn/o/sdm#Model\",\"https://w3id.org/okn/o/sdm#Theory-GuidedModel\"]}")
curl -X GET "$SERVER/v1.0.0/models/$MODEL_ID?username=mint@isi.edu" -H "accept: application/json" |  jq -r "."
