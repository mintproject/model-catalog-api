import connexion

from openapi_server.models.parameter import Parameter  # noqa: E501
import openapi_server.static_vars as staticvars


def obtain_uri(id):
    #todo: magic
    return staticvars.DEFAULT_MINT_INSTANCE + id


def create_parameter(parameter):  # noqa: E501
    """Create a Parameter

    Creates a new instance of a &#x60;Parameter&#x60;. # noqa: E501

    :param parameter: A new &#x60;Parameter&#x60; to be created.
    :type parameter: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        parameter = Parameter.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_parameters():  # noqa: E501
    """List All Parameters

    Gets a list of all &#x60;Parameter&#x60; entities. # noqa: E501


    :rtype: List[Parameter]
    """
    return 'do some magic!'
