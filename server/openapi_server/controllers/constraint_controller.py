import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CONSTRAINT_TYPE_NAME, CONSTRAINT_TYPE_URI

from openapi_server.models.constraint import Constraint  # noqa: E501
from openapi_server import util

def constraints_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Constraint

    Gets a list of all instances of Constraint (more information in https://w3id.org/okn/o/sdm#Constraint) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Constraint]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CONSTRAINT_TYPE_URI,
        rdf_type_name=CONSTRAINT_TYPE_NAME, 
        kls=Constraint)

def constraints_id_delete(id, user=None):  # noqa: E501
    """Delete an existing Constraint

    Delete an existing Constraint (more information in https://w3id.org/okn/o/sdm#Constraint) # noqa: E501

    :param id: The ID of the Constraint to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,
        user=user,
        rdf_type_uri=CONSTRAINT_TYPE_URI,
        rdf_type_name=CONSTRAINT_TYPE_NAME, 
        kls=Constraint)

def constraints_id_get(id, username=None):  # noqa: E501
    """Get a single Constraint by its id

    Gets the details of a given Constraint (more information in https://w3id.org/okn/o/sdm#Constraint) # noqa: E501

    :param id: The ID of the Constraint to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: Constraint
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=CONSTRAINT_TYPE_URI,
        rdf_type_name=CONSTRAINT_TYPE_NAME, 
        kls=Constraint)

def constraints_id_put(id, user=None, constraint=None):  # noqa: E501
    """Update an existing Constraint

    Updates an existing Constraint (more information in https://w3id.org/okn/o/sdm#Constraint) # noqa: E501

    :param id: The ID of the Constraint to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param constraint: An old Constraintto be updated
    :type constraint: dict | bytes

    :rtype: Constraint
    """

    if connexion.request.is_json:
        constraint = Constraint.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,
        user=user,
        body=constraint,
        rdf_type_uri=CONSTRAINT_TYPE_URI,
        rdf_type_name=CONSTRAINT_TYPE_NAME, 
        kls=Constraint)

def constraints_post(user=None, constraint=None):  # noqa: E501
    """Create one Constraint

    Create a new instance of Constraint (more information in https://w3id.org/okn/o/sdm#Constraint) # noqa: E501

    :param user: Username
    :type user: str
    :param constraint: Information about the Constraintto be created
    :type constraint: dict | bytes

    :rtype: Constraint
    """

    if connexion.request.is_json:
        constraint = Constraint.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(
        user=user,
        body=constraint,
        rdf_type_uri=CONSTRAINT_TYPE_URI,
        rdf_type_name=CONSTRAINT_TYPE_NAME, 
        kls=Constraint)
