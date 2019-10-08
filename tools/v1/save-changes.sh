SERVER_DIR=server
cp -rv $SERVER_DIR/openapi_server/settings server-v1.0.0/openapi_server/utils .openapi-generator/template/static_files/
cp -rv $SERVER_DIR/openapi_server/controllers/user_controller.py .openapi-generator/template/static_files/
cp -rv $SERVER_DIR/queries .openapi-generator/template/static_files/
cp -rv $SERVER_DIR/contexts .openapi-generator/template/static_files/
