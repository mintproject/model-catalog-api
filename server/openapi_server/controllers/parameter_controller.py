import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import PARAMETER_TYPE_NAME, PARAMETER_TYPE_URI

from openapi_server.models.parameter import Parameter  # noqa: E501
from openapi_server import util

def parameters_get(username=None, label=None):  # noqa: E501
    """List all Parameter entities

    Gets a list of all Parameter entities # noqa: E501

    :param username: Username to query
    :type username: str
    :param label: Filter by label
    :type label: str

    :rtype: List[Parameter]
    """


    return get_resource(
        username=username,
        label=label,
        rdf_type_uri=PARAMETER_TYPE_URI,
        rdf_type_name=PARAMETER_TYPE_NAME, 
        kls=Parameter)

def parameters_id_delete(id, user):  # noqa: E501
    """Delete a Parameter

    Delete an existing Parameter # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=PARAMETER_TYPE_URI,
        rdf_type_name=PARAMETER_TYPE_NAME, 
        kls=Parameter)

def parameters_id_get(id, username=None):  # noqa: E501
    """Get a Parameter

    Gets the details of a single instance of a Parameter # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: Parameter
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=PARAMETER_TYPE_URI,
        rdf_type_name=PARAMETER_TYPE_NAME, 
        kls=Parameter)

def parameters_id_put(id, user, parameter=None):  # noqa: E501
    """Update a Parameter

    Updates an existing Parameter # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param parameter: An old Parameterto be updated
    :type parameter: dict | bytes

    :rtype: Parameter
    """

    if connexion.request.is_json:
        parameter = Parameter.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=parameter,
        rdf_type_uri=PARAMETER_TYPE_URI,
        rdf_type_name=PARAMETER_TYPE_NAME, 
        kls=Parameter)

def parameters_post(user, parameter=None):  # noqa: E501
    """Create a Parameter

    Create a new instance of a Parameter # noqa: E501

    :param user: Username
    :type user: str
    :param parameter: A new Parameterto be created
    :type parameter: dict | bytes

    :rtype: Parameter
    """

    if connexion.request.is_json:
        parameter = Parameter.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=parameter,
        rdf_type_uri=PARAMETER_TYPE_URI,
        rdf_type_name=PARAMETER_TYPE_NAME, 
        kls=Parameter)
