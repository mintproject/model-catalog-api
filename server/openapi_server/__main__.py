#!/usr/bin/env python3

from openapi_server.cached import CachedSpecification
from connexion.spec import Specification

Specification.__init__ = CachedSpecification.__init__;
Specification.from_file = CachedSpecification.from_file

import connexion
from openapi_server import encoder

def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'Model Catalog'},
                pythonic_params=False)
    app.run(port=8080)


if __name__ == '__main__':
    main()
