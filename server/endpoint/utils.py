from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph
from openapi_server.static import UPDATE_ENDPOINT, DEFAULT_MINT_INSTANCE, QUERY_ENDPOINT
from openapi_server.static_vars import *
from flask import json
import requests
from pyld import jsonld


def update_panel_json(input_json, target_key):
    if isinstance(input_json, dict):
        for k, v in input_json.items():
            if k in target_key:
                input_json[target_key[k]] = input_json.pop(k)
            update_panel_json(v, target_key)

    elif isinstance(input_json, list):
        for item in input_json:
            update_panel_json(item, target_key)

def convert_to_json(resources_json_ld):
    update_key = {
        "@id": "id",
        "@type": "type"
    }

    expand = jsonld.expand(resources_json_ld)
    compact = jsonld.compact(expand, PREDICATE_CONTEXT)
    update_panel_json(compact, update_key)
    if '@graph' in compact:
        return compact['@graph']
    else:
        compact.pop('@context')
        return compact

def get_all_resource(resource_type, username=None):
    headers = {'Accept': 'application/ld+json'}
    query = query_all_resource(resource_type, username)
    data = {'query': query}
    resources_json_ld = requests.post(QUERY_ENDPOINT, headers=headers, data=data).json()
    resources_json = convert_to_json(resources_json_ld)
    return resources_json

def get_resource(resource_id, resource_type, username=None):
    headers = {'Accept': 'application/ld+json'}
    query = query_resource(resource_id, username)
    data = {'query': query}
    try:
        response = requests.post(QUERY_ENDPOINT, headers=headers, data=data)
        resources_json_ld = response.json()
        resources_json = convert_to_json(resources_json_ld)
    except Exception as e:
        print(e)
    return resources_json

def get_all_resources_related(resource_id, relation, username=None):
    headers = {'Accept': 'application/ld+json'}
    query = query_resource_related(resource_id, relation, username)
    data = {'query': query}
    resources_json_ld = requests.post(QUERY_ENDPOINT, headers=headers, data=data).json()
    resources_json = convert_to_json(resources_json_ld)
    return resources_json

def prepare_jsonld(resource, username, default_type):
    resource['@context'] = MINT_CONTEXT
    resource['@id'] = build_user_resource_uri(resource['id'])
    resource['@type'] = default_type
    for key in SUPPORTED_CLASSES:
        prepare_id_jsonld(resource, username, key)
    return json.dumps(resource)


def prepare_id_jsonld(json, username, key):
    if key in json:
        for item in json[key]:
            item['@id'] = build_user_resource_uri(item['id'])
            item['@type'] = [MAPPING_TYPE[key]]

            #include custom rdf:type
            if 'type' in item:
                for item_type in item['type']:
                    item['@type'].append(item_type)

def build_graph_uri(username):
    return f'{DEFAULT_MINT_INSTANCE}{username}_graph'


def build_user_resource_uri(resource):
    return f'{DEFAULT_MINT_INSTANCE}{resource}'


def execute_query(endpoint):
    if endpoint == '':
        return 'No SPARQL endpoint indicated', 407, {}


def select_query(endpoint, query):
    if endpoint == '':
        return 'No SPARQL endpoint indicated', 407, {}

    sparql = SPARQLWrapper(endpoint)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()


def insert_query(body, username):
    endpoint = UPDATE_ENDPOINT
    if endpoint == '':
        return 'No SPARQL endpoint indicated', 407, {}

    graph = build_graph_uri(username)
    prefixes, triples = prepare_jsonjd(body)
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


def prepare_jsonjd(jsonld):
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
