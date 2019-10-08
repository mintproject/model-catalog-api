import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import ICASAVARIABLE_TYPE_NAME, ICASAVARIABLE_TYPE_URI

from openapi_server.models.icasa_variable import ICASAVariable  # noqa: E501
from openapi_server import util

def icasavariables_get(username=None, label=None):  # noqa: E501
    """List all ICASAVariable entities

    Gets a list of all ICASAVariable entities # noqa: E501

    :param username: Username to query
    :type username: str
    :param label: Filter by label
    :type label: str

    :rtype: List[ICASAVariable]
    """


    return get_resource(
        username=username,
        label=label,
        rdf_type_uri=ICASAVARIABLE_TYPE_URI,
        rdf_type_name=ICASAVARIABLE_TYPE_NAME, 
        kls=ICASAVariable)

def icasavariables_id_delete(id, user):  # noqa: E501
    """Delete a ICASAVariable

    Delete an existing ICASAVariable # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=ICASAVARIABLE_TYPE_URI,
        rdf_type_name=ICASAVARIABLE_TYPE_NAME, 
        kls=ICASAVariable)

def icasavariables_id_get(id, username=None):  # noqa: E501
    """Get a ICASAVariable

    Gets the details of a single instance of a ICASAVariable # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: ICASAVariable
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=ICASAVARIABLE_TYPE_URI,
        rdf_type_name=ICASAVARIABLE_TYPE_NAME, 
        kls=ICASAVariable)

def icasavariables_id_put(id, user, icasa_variable=None):  # noqa: E501
    """Update a ICASAVariable

    Updates an existing ICASAVariable # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param icasa_variable: An old ICASAVariableto be updated
    :type icasa_variable: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        icasa_variable = ICASAVariable.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=icasa_variable,
        rdf_type_uri=ICASAVARIABLE_TYPE_URI,
        rdf_type_name=ICASAVARIABLE_TYPE_NAME, 
        kls=ICASAVariable)

def icasavariables_post(user, icasa_variable=None):  # noqa: E501
    """Create a ICASAVariable

    Create a new instance of a ICASAVariable # noqa: E501

    :param user: Username
    :type user: str
    :param icasa_variable: A new ICASAVariableto be created
    :type icasa_variable: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        icasa_variable = ICASAVariable.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=icasa_variable,
        rdf_type_uri=ICASAVARIABLE_TYPE_URI,
        rdf_type_name=ICASAVARIABLE_TYPE_NAME, 
        kls=ICASAVariable)
