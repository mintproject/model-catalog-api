from openapi_server import query_manager
from openapi_server.utils.vars import MODEL_TYPE_NAME, MODEL_TYPE_URI
from openapi_server.models.model import Model
from openapi_server import util

def health_get(username=None):  # noqa: E501
    """health_get

    Check if the service is up and running # noqa: E501


    :rtype: str
    """

    response = query_manager.get_resource(
            rdf_type_uri=MODEL_TYPE_URI,
            rdf_type_name=MODEL_TYPE_NAME, 
            username=username,
            kls=Model)

    response2 = query_manager.get_resource(
            id="TOPOFLOW",
            rdf_type_uri=MODEL_TYPE_URI,
            rdf_type_name=MODEL_TYPE_NAME, 
            username=username,
            kls=Model)
    
    if isinstance(response, tuple) and isinstance(response2, tuple):
        return "Bad request", 500, {}
    else:
        return "OK", 200, {}