from pathlib import Path

import yaml
from yaml import Loader

ref = "#/components/schemas"

def check_ref(schema, ref_schema_name):
    full_ref_schema = f"{ref}/{ref_schema_name}"
    for _, prop in schema['properties'].items():
        if "items" in prop and '$ref' in prop["items"] and prop["items"]['$ref'] == full_ref_schema:
            return True
    return False

config_yaml_path = Path('.') / "openapi.yaml"
spec = yaml.load(config_yaml_path.open(), Loader=Loader)
for key, schema in spec['components']['schemas'].items():
    for _, prop in schema['properties'].items():
        if "items" in prop and '$ref' in prop["items"]:
            ref_name = prop["items"]['$ref'].split('/')[-1]
            ref_schema = spec['components']['schemas'][ref_name]
            if check_ref(ref_schema, key):
                print(f"{key} - {ref_name}")
