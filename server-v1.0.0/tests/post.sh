DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source $DIR/env

TOKEN=$(curl -s -X GET "$SERVER/v1.0.0/user/login?username=mint%40isi.edu&password=mint123" -H "accept: application/json" | jq -r '.access_token')

#POST
echo "Inserting the model"
MODEL=$(curl -X POST "$SERVER/v1.0.0/models" -H "Authorization: Bearer $TOKEN" -H "accept: */*" -H "Content-Type: application/json" -d "{\"description\":[\"Decision Support System for Agrotechnology Transfer (DSSAT) is software application program that comprises dynamic crop growth simulation models for over 40 crops. DSSAT is supported by a range of utilities and applications for weather; soil; genetic; crop management and observational experimental data. Includes example data sets for all crop models. The crop simulation models simulate growth; development and yield as a function of the soil-plant-atmosphere dynamics (https://dssat.net/. 2019)\"],\"hasDocumentation\":[\"https://new.super.page.net\"],\"hasModelCategory\":[\"Agriculture\"],\"hasVersion\":[{\"id\":\"DSSAT_4.7\"}],\"id\":\"DSSAT\",\"label\":\"Decision Support System for Agrotechnology Transfer (DSSAT)\",\"type\":[\"https://w3id.org/okn/o/sdm#Model\",\"https://w3id.org/okn/o/sdm#Theory-GuidedModel\"]}")
MODEL_ID=$(echo $MODEL | jq -r '.id')
echo "ID model is: $MODEL_ID"
echo "Obtain the model"
curl -X GET "$SERVER/v1.0.0/models/$MODEL_ID?username=mint@isi.edu" -H "accept: application/json" | jq -r "."