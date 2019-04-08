#!/usr/bin/env python3

import connexion

from openapi_server import encoder
from openapi_server.config import app


def main():
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml', arguments={'title': 'Model Catalog'})
    app.run(port=8080)


if __name__ == '__main__':
    main()
