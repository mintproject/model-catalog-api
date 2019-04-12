from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph
from openapi_server.static import UPDATE_ENDPOINT, DEFAULT_MINT_INSTANCE, QUERY_ENDPOINT
from openapi_server.static_vars import *
from flask import json
import requests
import re
from pyld import jsonld
import six

def to_snake_name(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def to_camel_case(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def update_panel_json(input_json, target_key):
    if isinstance(input_json, dict):
        for k, v in input_json.items():
            #Obtain the rdf:type using the JSON key
            if k in SUPPORTED_CLASSES and type(v) == list:
                for item in v:
                    item['type'] = MAPPING_TYPE[k]
            elif k in SUPPORTED_CLASSES and type(v) == dict:
                v['type'] = MAPPING_TYPE[k]
            #Rename key to JSON-LD format
            if k in target_key:
                if k == 'id':
                    input_json[k] = build_user_resource_uri(input_json[k])
                #rename a key, for example @id -> id
                input_json[target_key[k]] = input_json.pop(k)

            update_panel_json(v, target_key)

    elif isinstance(input_json, list):
        for item in input_json:
            update_panel_json(item, target_key)

def type_to_json(input_json):
    if isinstance(input_json, dict):
        for k, v in input_json.items():
            #Obtain the rdf:type using the JSON key
            if k in SUPPORTED_CLASSES and type(v) == list:
                for item in v:
                    item['type'] = MAPPING_TYPE[k]
            elif k in SUPPORTED_CLASSES and type(v) == dict:
                v['type'] = MAPPING_TYPE[k]


    elif isinstance(input_json, list):
        for item in input_json:
            update_panel_json(item)

def verify_data_types(json, openapi_types):
    if '@type' in json and type(json['@type']) == str:
        json['@type'] = [json['@type']]

'''
Convert the internal json-ld to JSON with the API format
This method returns a array
json_convert must use embedding #10

'''
#todo: Is the same method for get and insert?
def convert_to_json(resources_json_ld, types):
    expand = jsonld.expand(resources_json_ld)
    compact = jsonld.compact(expand, PREDICATE_CONTEXT, {'compactArrays': False})
    if '@graph' in compact:
        return compact['@graph']
    else:
        compact.pop('@context')
        return compact

def get_all_resource(resource_type, types, username=None):
    headers = {'Accept': 'application/ld+json'}
    query = query_all_resource(resource_type, username)
    data = {'query': query}
    resources_json_ld = requests.post(QUERY_ENDPOINT, headers=headers, data=data).json()
    resources_json = convert_to_json(resources_json_ld, types)

    if not resources_json:
        resources_json = []
    elif resources_json and type(resources_json) == dict:
        resources_json = [resources_json]
    return resources_json

def get_resource(resource_id, resource_type, types, username=None):
    headers = {'Accept': 'application/ld+json'}
    query = query_resource(resource_id, username)
    data = {'query': query}
    try:
        response = requests.post(QUERY_ENDPOINT, headers=headers, data=data)
        resources_json_ld = response.json()
    except Exception as error:
        print(error)
    resources_json = convert_to_json(resources_json_ld, types)
    return resources_json

def get_all_resources_related(resource_id, relation, types, username=None):
    headers = {'Accept': 'application/ld+json'}
    query = query_resource_related(resource_id, relation, username)
    data = {'query': query}
    resources_json_ld = requests.post(QUERY_ENDPOINT, headers=headers, data=data).json()
    resources_json = convert_to_json(resources_json_ld, types)
    return resources_json

def prepare_jsonld(resource, username, default_type=None, attributes_map=None):

    update_key = {
        "id": "@id",
        "type": "@type"
    }

    resource_dict = resource.to_dict()
    resource_dict['@context'] = MINT_CONTEXT
    update_panel_json(resource_dict, update_key)
    resource_json = json.dumps(resource_dict)

    return resource_json

def get_type_resource(resource_type):
    return MAPPING_TYPE[resource_type]


def build_graph_uri(username):
    return f'{DEFAULT_MINT_INSTANCE}{username}_graph'



def build_user_resource_uri(resource):
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    if not re.match(regex, resource):
        return f'{DEFAULT_MINT_INSTANCE}{resource}'
    else:
        return resource


def insert_query(body, username):
    endpoint = UPDATE_ENDPOINT
    if endpoint == '':
        return 'No SPARQL endpoint indicated', 407, {}

    graph = build_graph_uri(username)
    prefixes, triples = build_insert_query(body)
    prefixes = '\n'.join(prefixes)
    triples = '\n'.join(triples)

    if not graph or graph == '' or graph == 'default':
        return 'Default graph is read only', 403, {}

    query_string = f'{prefixes} INSERT DATA {{ GRAPH <{graph}> {{ {triples} }} }}'
    sparql = SPARQLWrapper(endpoint)
    sparql.method = 'POST'

    try:
        sparql.setQuery(query_string)
        sparql.query()
    except Exception as e:
        return "Error inserting query", 407, {}
    return "Created", 201, {}

'''
TODO: hack rdflib has some problems
https://github.com/RDFLib/rdflib/issues/899
delete this hack
'''


def separate_prefixes_triples(s):
    triples = []
    for line in s.split('\n'):
        if not line.startswith('@prefix'):
            triples.append(line)
    return triples


'''
TODO: rdflib has some problems
'''


def build_insert_query(jsonld):
    prefixes = []
    g = Graph().parse(data=jsonld, format='json-ld')

    s = g.serialize(format='turtle')
    for n in g.namespace_manager.namespaces():
        prefixes.append(f'PREFIX {n[0]}: <{n[1]}>')

    return prefixes, separate_prefixes_triples(s.decode())


def query_all_resource(resource_type, username):
    if username:
        graph_uri = build_graph_uri(username)
        query = f'''PREFIX mc: <https://w3id.org/mint/modelCatalog#>
        CONSTRUCT {{
        ?s ?o ?p 
        }}
        WHERE {{
            GRAPH <{graph_uri}> {{
                ?s a {resource_type} .
                ?s ?o ?p
            }}
        }}
        '''
    else:
        query = f'''PREFIX mc: <https://w3id.org/mint/modelCatalog#>
        CONSTRUCT {{
        ?s ?o ?p 
        }}
        WHERE {{
            ?s a {resource_type} .
            ?s ?o ?p
        }}
        '''
    return query


def query_resource_related(resource_uri, relation, username):
    if username:
        graph_uri = build_graph_uri(username)
        query = f'''PREFIX mc: <https://w3id.org/mint/modelCatalog#>
        CONSTRUCT {{
        ?s ?o ?p 
        }}
        WHERE {{
            GRAPH <{graph_uri}> {{
                <{resource_uri}> {relation} ?s . 
                ?s ?o ?p
            }}
        }}
        '''
    else:
        query = f'''PREFIX mc: <https://w3id.org/mint/modelCatalog#>
        CONSTRUCT {{
        ?s ?o ?p 
        }}
        WHERE {{
            <{resource_uri}> {relation} ?s .
            ?s ?o ?p
        }}
        '''
    return query


def query_resource(resource_id, username):
    resource_uri = build_user_resource_uri(resource_id)
    if username:
        graph_uri = build_graph_uri(username)

        query = f'''PREFIX mc: <https://w3id.org/mint/modelCatalog#>
        CONSTRUCT {{
        <{resource_uri}> ?o ?p
        }}
        WHERE {{
            GRAPH <{graph_uri}> {{
                <{resource_uri}> ?o ?p
            }}
        }}
        '''
    else:
        query = f'''PREFIX mc: <https://w3id.org/mint/modelCatalog#>
        CONSTRUCT {{
            <{resource_uri}> ?o ?p
        }}
        WHERE {{
            <{resource_uri}> ?o ?p
        }}
        '''
    return query
