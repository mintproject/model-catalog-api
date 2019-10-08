import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import VARIABLEPRESENTATION_TYPE_NAME, VARIABLEPRESENTATION_TYPE_URI

from openapi_server.models.variable_presentation import VariablePresentation  # noqa: E501
from openapi_server import util

def variablepresentations_get(username=None, label=None):  # noqa: E501
    """List all VariablePresentation entities

    Gets a list of all VariablePresentation entities # noqa: E501

    :param username: Username to query
    :type username: str
    :param label: Filter by label
    :type label: str

    :rtype: List[VariablePresentation]
    """


    return get_resource(
        username=username,
        label=label,
        rdf_type_uri=VARIABLEPRESENTATION_TYPE_URI,
        rdf_type_name=VARIABLEPRESENTATION_TYPE_NAME, 
        kls=VariablePresentation)

def variablepresentations_id_delete(id, user):  # noqa: E501
    """Delete a VariablePresentation

    Delete an existing VariablePresentation # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=VARIABLEPRESENTATION_TYPE_URI,
        rdf_type_name=VARIABLEPRESENTATION_TYPE_NAME, 
        kls=VariablePresentation)

def variablepresentations_id_get(id, username=None):  # noqa: E501
    """Get a VariablePresentation

    Gets the details of a single instance of a VariablePresentation # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: VariablePresentation
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=VARIABLEPRESENTATION_TYPE_URI,
        rdf_type_name=VARIABLEPRESENTATION_TYPE_NAME, 
        kls=VariablePresentation)

def variablepresentations_id_put(id, user, variable_presentation=None):  # noqa: E501
    """Update a VariablePresentation

    Updates an existing VariablePresentation # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param variable_presentation: An old VariablePresentationto be updated
    :type variable_presentation: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        variable_presentation = VariablePresentation.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=variable_presentation,
        rdf_type_uri=VARIABLEPRESENTATION_TYPE_URI,
        rdf_type_name=VARIABLEPRESENTATION_TYPE_NAME, 
        kls=VariablePresentation)

def variablepresentations_post(user, variable_presentation=None):  # noqa: E501
    """Create a VariablePresentation

    Create a new instance of a VariablePresentation # noqa: E501

    :param user: Username
    :type user: str
    :param variable_presentation: A new VariablePresentationto be created
    :type variable_presentation: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        variable_presentation = VariablePresentation.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=variable_presentation,
        rdf_type_uri=VARIABLEPRESENTATION_TYPE_URI,
        rdf_type_name=VARIABLEPRESENTATION_TYPE_NAME, 
        kls=VariablePresentation)
