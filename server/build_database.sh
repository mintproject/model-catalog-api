#!/bin/sh

FILE=openapi/database/server.db
if [[ ! -f "$FILE" ]]; then
    python build_database.py
fi
