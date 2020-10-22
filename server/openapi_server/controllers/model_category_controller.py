import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MODELCATEGORY_TYPE_NAME, MODELCATEGORY_TYPE_URI

from openapi_server.models.model_category import ModelCategory  # noqa: E501
from openapi_server import util

def modelcategorys_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of ModelCategory

    Gets a list of all instances of ModelCategory (more information in https://w3id.org/okn/o/sdm#ModelCategory) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[ModelCategory]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MODELCATEGORY_TYPE_URI,
        rdf_type_name=MODELCATEGORY_TYPE_NAME, 
        kls=ModelCategory)

def modelcategorys_id_delete(id, user):  # noqa: E501
    """Delete an existing ModelCategory

    Delete an existing ModelCategory (more information in https://w3id.org/okn/o/sdm#ModelCategory) # noqa: E501

    :param id: The ID of the ModelCategory to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=MODELCATEGORY_TYPE_URI,
        rdf_type_name=MODELCATEGORY_TYPE_NAME, 
        kls=ModelCategory)

def modelcategorys_id_get(id, username=None):  # noqa: E501
    """Get a single ModelCategory by its id

    Gets the details of a given ModelCategory (more information in https://w3id.org/okn/o/sdm#ModelCategory) # noqa: E501

    :param id: The ID of the ModelCategory to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: ModelCategory
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=MODELCATEGORY_TYPE_URI,
        rdf_type_name=MODELCATEGORY_TYPE_NAME, 
        kls=ModelCategory)

def modelcategorys_id_put(id, user, model_category=None):  # noqa: E501
    """Update an existing ModelCategory

    Updates an existing ModelCategory (more information in https://w3id.org/okn/o/sdm#ModelCategory) # noqa: E501

    :param id: The ID of the ModelCategory to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param model_category: An old ModelCategoryto be updated
    :type model_category: dict | bytes

    :rtype: ModelCategory
    """

    if connexion.request.is_json:
        model_category = ModelCategory.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=model_category,
        rdf_type_uri=MODELCATEGORY_TYPE_URI,
        rdf_type_name=MODELCATEGORY_TYPE_NAME, 
        kls=ModelCategory)

def modelcategorys_post(user, model_category=None):  # noqa: E501
    """Create one ModelCategory

    Create a new instance of ModelCategory (more information in https://w3id.org/okn/o/sdm#ModelCategory) # noqa: E501

    :param user: Username
    :type user: str
    :param model_category: Information about the ModelCategoryto be created
    :type model_category: dict | bytes

    :rtype: ModelCategory
    """

    if connexion.request.is_json:
        model_category = ModelCategory.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=model_category,
        rdf_type_uri=MODELCATEGORY_TYPE_URI,
        rdf_type_name=MODELCATEGORY_TYPE_NAME, 
        kls=ModelCategory)
