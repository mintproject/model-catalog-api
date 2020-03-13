#!/usr/bin/env python3

import logging

import connexion
import yaml
from connexion.spec import Specification
from flask_testing import TestCase
from obasparql import QueryManager

from openapi_server import QUERY_DIRECTORY, CONTEXT_DIRECTORY, QUERIES_TYPES
from openapi_server.cached import CachedSpecification
from openapi_server.encoder import JSONEncoder

query_manager = QueryManager(queries_dir=QUERY_DIRECTORY,
                             context_dir=CONTEXT_DIRECTORY,
                             queries_types=QUERIES_TYPES)

import logging.config

with open('logging.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)
class BaseTestCase(TestCase):
    logger = logging.getLogger(__name__)


    def setup(self):
        self.get_username = "mint@isi.edu"

    def create_app(self):
        logger = logging.getLogger(__name__)
        Specification.from_file = CachedSpecification.from_file

        app = connexion.App(__name__, specification_dir='../openapi/')
        app.app.json_encoder = JSONEncoder
        app.add_api('openapi.yaml',
                    arguments={'title': 'Model Catalog'},
                    pythonic_params=False,
                    validate_responses=True)
        return app.app
