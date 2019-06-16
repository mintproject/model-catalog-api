#!/bin/sh

sed -i "s/username_var/${MYSQL_USER}/" config.ini
sed -i "s/password_var/${MYSQL_PASSWORD}/" config.ini
sed -i "s/host_var/${MYSQL_HOST}/" config.ini
sed -i "s/port_var/${MYSQL_PORT}/" config.ini
sed -i "s/database_name_var/${MYSQL_DATABASE}/" config.ini

python build_database.py
python -m openapi_server
