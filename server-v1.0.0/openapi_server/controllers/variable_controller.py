import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import VARIABLE_TYPE_NAME, VARIABLE_TYPE_URI

from openapi_server.models.variable import Variable  # noqa: E501
from openapi_server import util

def variables_get(username=None, query_text=None):  # noqa: E501
    """List all Variable entities

    Gets a list of all Variable entities # noqa: E501

    :param username: Username to query
    :type username: str
    :param query_text: A value of type string that will substitute ?_text in the original query
    :type query_text: str

    :rtype: List[Variable]
    """


    return get_resource(
        username=username,
        query_text=query_text,
        rdf_type_uri=VARIABLE_TYPE_URI,
        rdf_type_name=VARIABLE_TYPE_NAME, 
        kls=Variable)

def variables_id_delete(id, user):  # noqa: E501
    """Delete a Variable

    Delete an existing Variable # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=VARIABLE_TYPE_URI,
        rdf_type_name=VARIABLE_TYPE_NAME, 
        kls=Variable)

def variables_id_get(id, username=None):  # noqa: E501
    """Get a Variable

    Gets the details of a single instance of a Variable # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: Variable
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=VARIABLE_TYPE_URI,
        rdf_type_name=VARIABLE_TYPE_NAME, 
        kls=Variable)

def variables_id_put(id, user, variable=None):  # noqa: E501
    """Update a Variable

    Updates an existing Variable # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param variable: An old Variableto be updated
    :type variable: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        variable = Variable.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=variable,
        rdf_type_uri=VARIABLE_TYPE_URI,
        rdf_type_name=VARIABLE_TYPE_NAME, 
        kls=Variable)

def variables_post(user, variable=None):  # noqa: E501
    """Create a Variable

    Create a new instance of a Variable # noqa: E501

    :param user: Username
    :type user: str
    :param variable: A new Variableto be created
    :type variable: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        variable = Variable.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=variable,
        rdf_type_uri=VARIABLE_TYPE_URI,
        rdf_type_name=VARIABLE_TYPE_NAME, 
        kls=Variable)
