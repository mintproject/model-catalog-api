from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph

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


def zinsert_query(endpoint, body, graph):
    if endpoint == '':
        return 'No SPARQL endpoint indicated', 407, {}

    prefixes, triples = prepare_jsonjd(body)
    prefixes = '\n'.join(prefixes)
    triples = '\n'.join(triples)

    query_string = f'{prefixes} INSERT DATA {{ GRAPH <{graph}> {{ {triples} }} }}'
    sparql = SPARQLWrapper(endpoint)
    sparql.setQuery(query_string)
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


def prepare_jsonjd(jsonld):
    prefixes = []
    g = Graph().parse(data=jsonld, format='json-ld')

    s = g.serialize(format='turtle')
    for n in g.namespace_manager.namespaces():
        prefixes.append(f'PREFIX {n[0]}: <{n[1]}>')

    return prefixes, separate_prefixes_triples(s.decode())


