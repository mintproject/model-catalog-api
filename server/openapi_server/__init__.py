from obasparql import QueryManager
from openapi_server.settings import *

query_manager = QueryManager(
    endpoint=ENDPOINT,
    endpoint_username=ENDPOINT_USERNAME,
    endpoint_password=ENDPOINT_PASSWORD,
    queries_dir=QUERY_DIRECTORY,
    context_dir=CONTEXT_DIRECTORY,
    named_graph_base=ENDPOINT_GRAPH_BASE,
    uri_prefix=ENDPOINT_RESOURCE_PREFIX)

import logging.config
import os

# Disable Django's logging setup
LOGGING_CONFIG = None

LOGLEVEL = os.environ.get('LOGLEVEL', 'info').upper()

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            # exact format is not important, this is the minimum information
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        },
    },
    'handlers': {
        # console logs to stderr
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
    },
    'loggers': {
        # default for all undefined Python modules
        '': {
            'level': 'WARNING',
            'handlers': ['console'],
        },
        # Our application code
        'openapi_server': {
            'level': LOGLEVEL,
            'handlers': ['console'],
            # Avoid double logging because of root logger
            'propagate': False,
        },
        # Prevent noisy modules from logging to Sentry
        'noisy_module': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
    },
})
logger = logging.getLogger(__name__)

