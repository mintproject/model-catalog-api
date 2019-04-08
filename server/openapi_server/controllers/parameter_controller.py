import connexion

from openapi_server.models.parameter import Parameter  # noqa: E501
import openapi_server.static_vars as staticvars
from endpoint.utils import insert_query, prepare_jsonld, get_all_resource
from openapi_server.static_vars import *

def create_parameter(parameter, user):  # noqa: E501
    """Create a Parameter

    Creates a new instance of a &#x60;Parameter&#x60;. # noqa: E501

    :param parameter: A new &#x60;Parameter&#x60; to be created.
    :type parameter: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        _ = Parameter.from_dict(connexion.request.get_json())  # noqa: E501
        parameter_json = prepare_jsonld(connexion.request.get_json(), user, PARAMETER_TYPE)
        return insert_query(parameter_json, user)

    return "Bad request", 400, {}


def get_parameters():  # noqa: E501
    """List All Parameters

    Gets a list of all &#x60;Parameter&#x60; entities. # noqa: E501


    :rtype: List[Parameter]
    """
    try:
        return get_all_resource(PARAMETER_TYPE)
    except:
        return "Bad request", 400, {}
