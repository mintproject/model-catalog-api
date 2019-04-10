#!/bin/sh

FILE=openapi_server/database/server.db
if [[ ! -f "$FILE" ]]; then
    python build_database.py
fi

python -m openapi_server
