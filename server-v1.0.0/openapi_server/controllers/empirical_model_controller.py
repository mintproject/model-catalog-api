import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import EMPIRICALMODEL_TYPE_NAME, EMPIRICALMODEL_TYPE_URI

from openapi_server.models.empirical_model import EmpiricalModel  # noqa: E501
from openapi_server import util

def empiricalmodels_get(username=None, query_text=None):  # noqa: E501
    """List all EmpiricalModel entities

    Gets a list of all EmpiricalModel entities # noqa: E501

    :param username: Username to query
    :type username: str
    :param query_text: A value of type string that will substitute ?_text in the original query
    :type query_text: str

    :rtype: List[EmpiricalModel]
    """


    return get_resource(
        username=username,
        query_text=query_text,
        rdf_type_uri=EMPIRICALMODEL_TYPE_URI,
        rdf_type_name=EMPIRICALMODEL_TYPE_NAME, 
        kls=EmpiricalModel)

def empiricalmodels_id_delete(id, user):  # noqa: E501
    """Delete a EmpiricalModel

    Delete an existing EmpiricalModel # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=EMPIRICALMODEL_TYPE_URI,
        rdf_type_name=EMPIRICALMODEL_TYPE_NAME, 
        kls=EmpiricalModel)

def empiricalmodels_id_get(id, username=None):  # noqa: E501
    """Get a EmpiricalModel

    Gets the details of a single instance of a EmpiricalModel # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: EmpiricalModel
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=EMPIRICALMODEL_TYPE_URI,
        rdf_type_name=EMPIRICALMODEL_TYPE_NAME, 
        kls=EmpiricalModel)

def empiricalmodels_id_put(id, user, empirical_model=None):  # noqa: E501
    """Update a EmpiricalModel

    Updates an existing EmpiricalModel # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param empirical_model: An old EmpiricalModelto be updated
    :type empirical_model: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        empirical_model = EmpiricalModel.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=empirical_model,
        rdf_type_uri=EMPIRICALMODEL_TYPE_URI,
        rdf_type_name=EMPIRICALMODEL_TYPE_NAME, 
        kls=EmpiricalModel)

def empiricalmodels_post(user, empirical_model=None):  # noqa: E501
    """Create a EmpiricalModel

    Create a new instance of a EmpiricalModel # noqa: E501

    :param user: Username
    :type user: str
    :param empirical_model: A new EmpiricalModelto be created
    :type empirical_model: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        empirical_model = EmpiricalModel.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=empirical_model,
        rdf_type_uri=EMPIRICALMODEL_TYPE_URI,
        rdf_type_name=EMPIRICALMODEL_TYPE_NAME, 
        kls=EmpiricalModel)
