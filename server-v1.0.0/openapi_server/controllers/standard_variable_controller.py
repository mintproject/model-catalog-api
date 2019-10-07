import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import STANDARDVARIABLE_TYPE_NAME, STANDARDVARIABLE_TYPE_URI

from openapi_server.models.standard_variable import StandardVariable  # noqa: E501
from openapi_server import util

def standardvariables_get(username=None, query_text=None):  # noqa: E501
    """List all StandardVariable entities

    Gets a list of all StandardVariable entities # noqa: E501

    :param username: Username to query
    :type username: str
    :param query_text: A value of type string that will substitute ?_text in the original query
    :type query_text: str

    :rtype: List[StandardVariable]
    """


    return get_resource(
        username=username,
        query_text=query_text,
        rdf_type_uri=STANDARDVARIABLE_TYPE_URI,
        rdf_type_name=STANDARDVARIABLE_TYPE_NAME, 
        kls=StandardVariable)

def standardvariables_id_delete(id, user):  # noqa: E501
    """Delete a StandardVariable

    Delete an existing StandardVariable # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=STANDARDVARIABLE_TYPE_URI,
        rdf_type_name=STANDARDVARIABLE_TYPE_NAME, 
        kls=StandardVariable)

def standardvariables_id_get(id, username=None):  # noqa: E501
    """Get a StandardVariable

    Gets the details of a single instance of a StandardVariable # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: StandardVariable
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=STANDARDVARIABLE_TYPE_URI,
        rdf_type_name=STANDARDVARIABLE_TYPE_NAME, 
        kls=StandardVariable)

def standardvariables_id_put(id, user, standard_variable=None):  # noqa: E501
    """Update a StandardVariable

    Updates an existing StandardVariable # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param standard_variable: An old StandardVariableto be updated
    :type standard_variable: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        standard_variable = StandardVariable.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=standard_variable,
        rdf_type_uri=STANDARDVARIABLE_TYPE_URI,
        rdf_type_name=STANDARDVARIABLE_TYPE_NAME, 
        kls=StandardVariable)

def standardvariables_post(user, standard_variable=None):  # noqa: E501
    """Create a StandardVariable

    Create a new instance of a StandardVariable # noqa: E501

    :param user: Username
    :type user: str
    :param standard_variable: A new StandardVariableto be created
    :type standard_variable: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        standard_variable = StandardVariable.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=standard_variable,
        rdf_type_uri=STANDARDVARIABLE_TYPE_URI,
        rdf_type_name=STANDARDVARIABLE_TYPE_NAME, 
        kls=StandardVariable)
