from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph, URIRef, Literal


# todo: detect type of query
def execute_query(endpoint, query):
    if endpoint == '':
        return 'No SPARQL endpoint indicated', 407, {}


def select_query(endpoint, query):
    if endpoint == '':
        return 'No SPARQL endpoint indicated', 407, {}

    sparql = SPARQLWrapper(endpoint)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()


def insert_query(endpoint, query):
    if endpoint == '':
        return 'No SPARQL endpoint indicated', 407, {}

    sparql = SPARQLWrapper(endpoint)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()


def insert_triples_hardcoding():
    graph = "http://example/bookStore"
    triples = "<http://example/boo21> <http://example.org/ns#price>  42 ."
    queryString = f'INSERT DATA {{ GRAPH <{graph}> {{ {triples} }} }}'
    endpoint = "http://ontosoft.isi.edu:3030/test/update"
    sparql = SPARQLWrapper(endpoint)
    sparql.setQuery(queryString)
    sparql.method = 'POST'
    sparql.query()


def insert_triples(graph, prefixes, triples):
    prefixes = '\n'.join(prefixes)
    triples = '\n'.join(triples)
    queryString = f'{prefixes} INSERT DATA {{ GRAPH <{graph}> {{ {triples} }} }}'
    endpoint = "http://ontosoft.isi.edu:3030/test/update"
    sparql = SPARQLWrapper(endpoint)
    sparql.setQuery(queryString)
    sparql.method = 'POST'
    sparql.query()


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


def prepare_jsonjd(triples_json):
    triples = []
    prefixes = []

    g = Graph().parse(data=triples_json, format='json-ld')
    s = g.serialize(format='turtle')
    for n in g.namespace_manager.namespaces():
        prefixes.append(f'PREFIX {n[0]}: <{n[1]}>')

    return prefixes, separate_prefixes_triples(s.decode())


'''
TODO: rdflib has some problems
'''


def better_prepare_jsonjd(triples_json):
    triples = []
    g = Graph().parse(data=triples_json, format='json-ld')
    s = g.serialize(format='turtle')
    for triple in g.triples():
        triples.append(triple)
    all_ns = [n for n in g.namespace_manager.namespaces()]
    return
    prefixes, triples = separate_prefixes_triples(s.decode())
    if prefixes and triples:
        return prefixes, triples
    else:
        return None, None


def main():
    test_json = '''
{
    "@context": {
        "qudt": "http://qudt.org/schema/qudt",
        "owl": "http://www.w3.org/2002/07/owl",
        "xsd": "http://www.w3.org/2001/XMLSchema",
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns",
        "purl": "http://purl.org/dc/terms/",
        "mc": "https://w3id.org/mint/modelCatalog#",
        "wingsexport": "https://w3id.org/wings/export/",
        "label": "rdf:label",
        "description": "purl:description",
        "cag": "mc:hasCAG",
        "inputs": "mc:hasInput",
        "outputs": "mc:hasOutput",
        "process": "mc:hasProcess",
        "intervaltime": "mc:hasTimeInterval",
        "implementationScriptLocation": "mc:hasImplementationScriptLocation",
        "container": "mc:hasContainer",
        "constrainT": "mc:hasConstraint",
        "parameters": "mc:hasParameter",
        "componentLocation": "mc:hasComponentLocation"
    },
    
    "@id": "https://w3id.org/mint/instance/economic",
    "uri": "https://w3id.org/mint/instance/economic",
    "@type": ["mc:ModelConfiguration"],
    "label": "Economic aggregate crop supply",
    "inputs": [
        {
            "@id": "https://w3id.org/mint/instance/econ_yield"
        }
    ],
    "outputs": [
        {
            "@id": "https://w3id.org/mint/instance/econ_land_use"
        }
    ],
    "description": "Aggregate crop supply response model for the country of South Sudan configuration",
    "cag": [
        {
            "@id": "https://w3id.org/mint/instance/economic_aggregate_crop_supply_CAG_variables"
        },
        {
            "@id": "https://w3id.org/mint/instance/economic_aggregate_crop_supply_CAG_process"
        }        
    ],
    "process": [
        {
            "@id": "https://w3id.org/mint/instance/crop_yield"
        },
        {
            "@id": "https://w3id.org/mint/instance/crop_supply"
        }        
    ],
    "intervalTime": [
        {
            "@id": "https://w3id.org/mint/instance/economic_aggregate_crop_supply_TI"
        }
    ],
    "implementationScriptLocation": "https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/MINT-WorkflowDomain/master/WINGSWorkflowComponents/economic/run",
    "container": "https://w3id.org/mint/instance/mintproject/economic:latest",
    "constrainT": "[ backwardPIHMInputsDataHaveSameRegion: (?c rdf:type acdom:pihmClass) (?c ac:hasInput ?in1) (?c ac:hasInput ?in2) noValue(?in1 dcdom:region) noValue(?in2 dcdom:region) uriConcat(?c '_region' ?location) -> (?in1 dcdom:region ?location) (?in2 dcdom:region ?location) print('Setting domain of ?in1 and ?in2 to ?location because both inputs to PIHM should be from the same region')]",
    "parameters": [
        {
            "@id": "https://w3id.org/mint/instance/pihm_start-date"
        },
        {
            "@id": "https://w3id.org/mint/instance/pihm_end-date"
        }        
    ],
    "componentLocation": "https://github.com/KnowledgeCaptureAndDiscovery/MINT-WorkflowDomain/raw/master/WINGSWorkflowComponents/economic/economic.zip"
}
  '''

    graph = "http://example/bookStore2"
    prefixes, triples = prepare_jsonjd(test_json)
    insert_triples(graph, prefixes, triples)


main()
