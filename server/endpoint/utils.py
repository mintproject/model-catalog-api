from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph
from openapi_server.static import UPDATE_ENDPOINT, DEFAULT_MINT_INSTANCE
from openapi_server.static_vars import *
from flask import json
import requests


def get_all_resource(resource_type):
    headers = {
        'Accept': 'application/ld+json',
    }
    query_resource = f'  ?s rdf:type {resource_type} .'
    data = {
        'query': 'PREFIX xml: <http://www.w3.org/XML/1998/namespace>'
                 'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>'
                 'PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>'
                 'PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>'
                 'PREFIX dc: <http://purl.org/dc/terms/>'
                 'PREFIX mc: <https://w3id.org/mint/modelCatalog#>'
                 'CONSTRUCT {'
                 '?s ?o ?p '
                 '}'
                 'WHERE {'
                 f'{query_resource}'
                 '?s ?o ?p'
                 '}'
    }

    return requests.post('http://ontosoft.isi.edu:3030/ds/query', headers=headers, data=data)


def get_resource(resource_id, resource_type):
    headers = {
        'Accept': 'application/ld+json',
    }
    resource_uri = build_user_resource_uri(resource_id)
    query_resource = f'<{resource_uri}> ?o ?p .'

    data = {
        'query': 'PREFIX xml: <http://www.w3.org/XML/1998/namespace>'
                 'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>'
                 'PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>'
                 'PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>'
                 'PREFIX dc: <http://purl.org/dc/terms/>'
                 'PREFIX mc: <https://w3id.org/mint/modelCatalog#>'
                 'CONSTRUCT {'
                 f'<{resource_uri}> ?o ?p '
                 '}'
                 'WHERE {'
                 f'{query_resource}'
                 '}'
    }

    return requests.post('http://ontosoft.isi.edu:3030/ds/query', headers=headers, data=data)


def get_all_resources_related(resource_id, relation):
    headers = {
        'Accept': 'application/ld+json',
    }
    resource_uri = build_user_resource_uri(resource_id)

    construct_clause = f'?s ?o ?p'
    where_clause = f'<{resource_uri}> {relation} ?s . ?s ?o ?p'

    data = {
        'query': 'PREFIX xml: <http://www.w3.org/XML/1998/namespace>'
                 'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>'
                 'PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>'
                 'PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>'
                 'PREFIX dc: <http://purl.org/dc/terms/>'
                 'PREFIX mc: <https://w3id.org/mint/modelCatalog#>'
                 'CONSTRUCT {'
                 f'{construct_clause}'
                 '}'
                 'WHERE {'
                 f'{where_clause}'
                 '}'
    }

    return requests.post('http://ontosoft.isi.edu:3030/ds/query', headers=headers, data=data)


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
        return e, 407, {}
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
