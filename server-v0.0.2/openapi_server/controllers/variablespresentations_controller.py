import connexion
import six

from openapi_server.models.variable_presentation import VariablePresentation  # noqa: E501
from openapi_server import util
from endpoint.utils import insert_query, prepare_jsonld, get_all_resource, get_resource, get_all_resources_related
from openapi_server.static_vars import *


def datasetspecification_id_variablepresentations_get(id, username=None):  # noqa: E501
    """List variable presentations related with a datasetspecification

    Gets a list of all &#x60;VariablePresentation&#x60; entities. # noqa: E501

    :param id: A unique identifier for a &#x60;DatasetSpecification&#x60;.
    :type id: str
    :param username: To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username
    :type username: str

    :rtype: List[VariablePresentation]
    """
    try:
        response = get_all_resources_related(id, HAS_PRESENTATION, VARIABLE_PRESENTATION_TYPE, username)
    except:
        return "Bad request", 400, {}
    vars = []
    for d in response:
        vars.append(VariablePresentation.from_dict(d))

    return vars
