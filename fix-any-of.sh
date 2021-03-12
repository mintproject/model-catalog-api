sed -i.bak 's/AnyOf[a-zA-Z]*/object/g' *.py
sed -i.bak.2 '/from openapi_server.models.any/d' *.py
