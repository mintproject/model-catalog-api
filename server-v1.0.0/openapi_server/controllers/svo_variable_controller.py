import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import SVOVARIABLE_TYPE_NAME, SVOVARIABLE_TYPE_URI

from openapi_server.models.svo_variable import SVOVariable  # noqa: E501
from openapi_server import util

def svovariables_get(username=None, query_text=None):  # noqa: E501
    """List all SVOVariable entities

    Gets a list of all SVOVariable entities # noqa: E501

    :param username: Username to query
    :type username: str
    :param query_text: A value of type string that will substitute ?_text in the original query
    :type query_text: str

    :rtype: List[SVOVariable]
    """


    return get_resource(
        username=username,
        query_text=query_text,
        rdf_type_uri=SVOVARIABLE_TYPE_URI,
        rdf_type_name=SVOVARIABLE_TYPE_NAME, 
        kls=SVOVariable)

def svovariables_id_delete(id, user):  # noqa: E501
    """Delete a SVOVariable

    Delete an existing SVOVariable # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=SVOVARIABLE_TYPE_URI,
        rdf_type_name=SVOVARIABLE_TYPE_NAME, 
        kls=SVOVariable)

def svovariables_id_get(id, username=None):  # noqa: E501
    """Get a SVOVariable

    Gets the details of a single instance of a SVOVariable # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: SVOVariable
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=SVOVARIABLE_TYPE_URI,
        rdf_type_name=SVOVARIABLE_TYPE_NAME, 
        kls=SVOVariable)

def svovariables_id_put(id, user, svo_variable=None):  # noqa: E501
    """Update a SVOVariable

    Updates an existing SVOVariable # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param svo_variable: An old SVOVariableto be updated
    :type svo_variable: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        svo_variable = SVOVariable.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=svo_variable,
        rdf_type_uri=SVOVARIABLE_TYPE_URI,
        rdf_type_name=SVOVARIABLE_TYPE_NAME, 
        kls=SVOVariable)

def svovariables_post(user, svo_variable=None):  # noqa: E501
    """Create a SVOVariable

    Create a new instance of a SVOVariable # noqa: E501

    :param user: Username
    :type user: str
    :param svo_variable: A new SVOVariableto be created
    :type svo_variable: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        svo_variable = SVOVariable.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=svo_variable,
        rdf_type_uri=SVOVARIABLE_TYPE_URI,
        rdf_type_name=SVOVARIABLE_TYPE_NAME, 
        kls=SVOVariable)
