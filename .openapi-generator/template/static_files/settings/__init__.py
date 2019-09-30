from configparser import ConfigParser
import os
# Setting headersto use access_token for the GitHub API
config_fallbacks = {
    'github_access_token': '',
    'endpoint': '',
    'user': '',
    'password': '',
    'server_name': '',
    'prefix': '',
    'graph_base': '',
    'firebase_key': '',
    'local_sparql_dir': ''

}
config = ConfigParser(config_fallbacks)
config.add_section('auth')
config.add_section('defaults')
config.add_section('local')
config.read('config.ini')
config_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config.ini')
config.read(config_filename)

# Default endpoint, if none specified elsewhere
ENDPOINT = config.get('defaults', 'endpoint')
ENDPOINT_USER = config.get('defaults', 'user')
ENDPOINT_PASSWORD = config.get('defaults', 'password')
PREFIX = config.get('defaults', 'prefix')
GRAPH_BASE = config.get('defaults', 'graph_base')
FIREBASE_KEY = config.get('defaults', 'firebase_key')
UPDATE_ENDPOINT = f'{ENDPOINT}/update'
QUERY_ENDPOINT = f'{ENDPOINT}/query'

QUERY_DIRECTORY = "/Users/mosorio/repos/isi/MINT-ModelCatalogIngestionAPI/server-v1.0.0/queries/"
CONTEXT_DIRECTORY = "/Users/mosorio/repos/isi/MINT-ModelCatalogIngestionAPI/server-v1.0.0/contexts/"

mime_types = {
    'csv': 'text/csv; q=1.0, */*; q=0.1',
    'json': 'application/json; q=1.0, application/sparql-results+json; q=0.8, */*; q=0.1',
    'html': 'text/html; q=1.0, */*; q=0.1',
    'ttl': 'text/turtle'
}

QUERIES_TYPES = ["get_all", "get_all_related", "get_all_related_user", "get_all_user", "get_one", "get_one_user"]


