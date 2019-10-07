import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import HYBRIDMODEL_TYPE_NAME, HYBRIDMODEL_TYPE_URI

from openapi_server.models.hybrid_model import HybridModel  # noqa: E501
from openapi_server import util

def hybridmodels_get(username=None, query_text=None):  # noqa: E501
    """List all HybridModel entities

    Gets a list of all HybridModel entities # noqa: E501

    :param username: Username to query
    :type username: str
    :param query_text: A value of type string that will substitute ?_text in the original query
    :type query_text: str

    :rtype: List[HybridModel]
    """


    return get_resource(
        username=username,
        query_text=query_text,
        rdf_type_uri=HYBRIDMODEL_TYPE_URI,
        rdf_type_name=HYBRIDMODEL_TYPE_NAME, 
        kls=HybridModel)

def hybridmodels_id_delete(id, user):  # noqa: E501
    """Delete a HybridModel

    Delete an existing HybridModel # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=HYBRIDMODEL_TYPE_URI,
        rdf_type_name=HYBRIDMODEL_TYPE_NAME, 
        kls=HybridModel)

def hybridmodels_id_get(id, username=None):  # noqa: E501
    """Get a HybridModel

    Gets the details of a single instance of a HybridModel # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: HybridModel
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=HYBRIDMODEL_TYPE_URI,
        rdf_type_name=HYBRIDMODEL_TYPE_NAME, 
        kls=HybridModel)

def hybridmodels_id_put(id, user, hybrid_model=None):  # noqa: E501
    """Update a HybridModel

    Updates an existing HybridModel # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param hybrid_model: An old HybridModelto be updated
    :type hybrid_model: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        hybrid_model = HybridModel.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=hybrid_model,
        rdf_type_uri=HYBRIDMODEL_TYPE_URI,
        rdf_type_name=HYBRIDMODEL_TYPE_NAME, 
        kls=HybridModel)

def hybridmodels_post(user, hybrid_model=None):  # noqa: E501
    """Create a HybridModel

    Create a new instance of a HybridModel # noqa: E501

    :param user: Username
    :type user: str
    :param hybrid_model: A new HybridModelto be created
    :type hybrid_model: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        hybrid_model = HybridModel.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=hybrid_model,
        rdf_type_uri=HYBRIDMODEL_TYPE_URI,
        rdf_type_name=HYBRIDMODEL_TYPE_NAME, 
        kls=HybridModel)
