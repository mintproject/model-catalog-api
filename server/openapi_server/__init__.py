from obasparql import QueryManager
from openapi_server.settings import *
import logging

try:
    logging.config.fileConfig(logging_file)
except:
    logging.error("Logging config file does not exist {}".format(logging_file))
    exit(0)

logger = logging.getLogger(__name__)

query_manager = QueryManager(
    endpoint=ENDPOINT,
    endpoint_username=ENDPOINT_USERNAME,
    endpoint_password=ENDPOINT_PASSWORD,
    queries_dir=QUERY_DIRECTORY,
    context_dir=CONTEXT_DIRECTORY,
    named_graph_base=ENDPOINT_GRAPH_BASE,
    uri_prefix=ENDPOINT_RESOURCE_PREFIX)

#!/usr/bin/env python3

from openapi_server.cached import CachedSpecification
from connexion.spec import Specification

Specification.__init__ = CachedSpecification.__init__;
Specification.from_file = CachedSpecification.from_file

import connexion
from openapi_server import encoder

app = connexion.App(__name__, specification_dir='./openapi/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('openapi.yaml',
            arguments={'title': 'model catalog'},
            pythonic_params=False)