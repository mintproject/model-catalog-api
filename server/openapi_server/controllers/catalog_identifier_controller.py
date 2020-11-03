import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CATALOGIDENTIFIER_TYPE_NAME, CATALOGIDENTIFIER_TYPE_URI

from openapi_server.models.catalog_identifier import CatalogIdentifier  # noqa: E501
from openapi_server import util

def catalogidentifiers_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of CatalogIdentifier

    Gets a list of all instances of CatalogIdentifier (more information in https://w3id.org/okn/o/sd#CatalogIdentifier) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[CatalogIdentifier]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CATALOGIDENTIFIER_TYPE_URI,
        rdf_type_name=CATALOGIDENTIFIER_TYPE_NAME, 
        kls=CatalogIdentifier)

def catalogidentifiers_id_delete(id, user):  # noqa: E501
    """Delete an existing CatalogIdentifier

    Delete an existing CatalogIdentifier (more information in https://w3id.org/okn/o/sd#CatalogIdentifier) # noqa: E501

    :param id: The ID of the CatalogIdentifier to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=CATALOGIDENTIFIER_TYPE_URI,
        rdf_type_name=CATALOGIDENTIFIER_TYPE_NAME, 
        kls=CatalogIdentifier)

def catalogidentifiers_id_get(id, username=None):  # noqa: E501
    """Get a single CatalogIdentifier by its id

    Gets the details of a given CatalogIdentifier (more information in https://w3id.org/okn/o/sd#CatalogIdentifier) # noqa: E501

    :param id: The ID of the CatalogIdentifier to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: CatalogIdentifier
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=CATALOGIDENTIFIER_TYPE_URI,
        rdf_type_name=CATALOGIDENTIFIER_TYPE_NAME, 
        kls=CatalogIdentifier)

def catalogidentifiers_id_put(id, user, catalog_identifier=None):  # noqa: E501
    """Update an existing CatalogIdentifier

    Updates an existing CatalogIdentifier (more information in https://w3id.org/okn/o/sd#CatalogIdentifier) # noqa: E501

    :param id: The ID of the CatalogIdentifier to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param catalog_identifier: An old CatalogIdentifierto be updated
    :type catalog_identifier: dict | bytes

    :rtype: CatalogIdentifier
    """

    if connexion.request.is_json:
        catalog_identifier = CatalogIdentifier.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=catalog_identifier,
        rdf_type_uri=CATALOGIDENTIFIER_TYPE_URI,
        rdf_type_name=CATALOGIDENTIFIER_TYPE_NAME, 
        kls=CatalogIdentifier)

def catalogidentifiers_post(user, catalog_identifier=None):  # noqa: E501
    """Create one CatalogIdentifier

    Create a new instance of CatalogIdentifier (more information in https://w3id.org/okn/o/sd#CatalogIdentifier) # noqa: E501

    :param user: Username
    :type user: str
    :param catalog_identifier: Information about the CatalogIdentifierto be created
    :type catalog_identifier: dict | bytes

    :rtype: CatalogIdentifier
    """

    if connexion.request.is_json:
        catalog_identifier = CatalogIdentifier.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=catalog_identifier,
        rdf_type_uri=CATALOGIDENTIFIER_TYPE_URI,
        rdf_type_name=CATALOGIDENTIFIER_TYPE_NAME, 
        kls=CatalogIdentifier)
