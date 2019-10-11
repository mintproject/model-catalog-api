import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import EQUATION_TYPE_NAME, EQUATION_TYPE_URI

from openapi_server.models.equation import Equation  # noqa: E501
from openapi_server import util

def equations_get(username=None, label=None):  # noqa: E501
    """List all Equation entities

    Gets a list of all Equation entities # noqa: E501

    :param username: Username to query
    :type username: str
    :param label: Filter by label
    :type label: str

    :rtype: List[Equation]
    """


    return get_resource(
        username=username,
        label=label,
        rdf_type_uri=EQUATION_TYPE_URI,
        rdf_type_name=EQUATION_TYPE_NAME, 
        kls=Equation)

def equations_id_delete(id, user):  # noqa: E501
    """Delete a Equation

    Delete an existing Equation # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=EQUATION_TYPE_URI,
        rdf_type_name=EQUATION_TYPE_NAME, 
        kls=Equation)

def equations_id_get(id, username=None):  # noqa: E501
    """Get a Equation

    Gets the details of a single instance of a Equation # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: Equation
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=EQUATION_TYPE_URI,
        rdf_type_name=EQUATION_TYPE_NAME, 
        kls=Equation)

def equations_id_put(id, user, equation=None):  # noqa: E501
    """Update a Equation

    Updates an existing Equation # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param equation: An old Equationto be updated
    :type equation: dict | bytes

    :rtype: Equation
    """

    if connexion.request.is_json:
        equation = Equation.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=equation,
        rdf_type_uri=EQUATION_TYPE_URI,
        rdf_type_name=EQUATION_TYPE_NAME, 
        kls=Equation)

def equations_post(user, equation=None):  # noqa: E501
    """Create a Equation

    Create a new instance of a Equation # noqa: E501

    :param user: Username
    :type user: str
    :param equation: A new Equationto be created
    :type equation: dict | bytes

    :rtype: Equation
    """

    if connexion.request.is_json:
        equation = Equation.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=equation,
        rdf_type_uri=EQUATION_TYPE_URI,
        rdf_type_name=EQUATION_TYPE_NAME, 
        kls=Equation)
