#!/bin/sh

python build_database.py
python -m openapi_server
