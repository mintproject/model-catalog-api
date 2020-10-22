import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import COUPLEDMODEL_TYPE_NAME, COUPLEDMODEL_TYPE_URI

from openapi_server.models.coupled_model import CoupledModel  # noqa: E501
from openapi_server import util

def coupledmodels_get(username=None, label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of CoupledModel

    Gets a list of all instances of CoupledModel (more information in https://w3id.org/okn/o/sdm#CoupledModel) # noqa: E501

    :param username: Name of the user graph to query
    :type username: str
    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[CoupledModel]
    """


    return query_manager.get_resource(
        username=username,
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=COUPLEDMODEL_TYPE_URI,
        rdf_type_name=COUPLEDMODEL_TYPE_NAME, 
        kls=CoupledModel)

def coupledmodels_id_delete(id, user):  # noqa: E501
    """Delete an existing CoupledModel

    Delete an existing CoupledModel (more information in https://w3id.org/okn/o/sdm#CoupledModel) # noqa: E501

    :param id: The ID of the CoupledModel to be retrieved
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return query_manager.delete_resource(id=id,user=user,
        rdf_type_uri=COUPLEDMODEL_TYPE_URI,
        rdf_type_name=COUPLEDMODEL_TYPE_NAME, 
        kls=CoupledModel)

def coupledmodels_id_get(id, username=None):  # noqa: E501
    """Get a single CoupledModel by its id

    Gets the details of a given CoupledModel (more information in https://w3id.org/okn/o/sdm#CoupledModel) # noqa: E501

    :param id: The ID of the CoupledModel to be retrieved
    :type id: str
    :param username: Name of the user graph to query
    :type username: str

    :rtype: CoupledModel
    """


    return query_manager.get_resource(id=id,
        username=username,
        rdf_type_uri=COUPLEDMODEL_TYPE_URI,
        rdf_type_name=COUPLEDMODEL_TYPE_NAME, 
        kls=CoupledModel)

def coupledmodels_id_put(id, user, coupled_model=None):  # noqa: E501
    """Update an existing CoupledModel

    Updates an existing CoupledModel (more information in https://w3id.org/okn/o/sdm#CoupledModel) # noqa: E501

    :param id: The ID of the CoupledModel to be retrieved
    :type id: str
    :param user: Username
    :type user: str
    :param coupled_model: An old CoupledModelto be updated
    :type coupled_model: dict | bytes

    :rtype: CoupledModel
    """

    if connexion.request.is_json:
        coupled_model = CoupledModel.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.put_resource(id=id,user=user,
        body=coupled_model,
        rdf_type_uri=COUPLEDMODEL_TYPE_URI,
        rdf_type_name=COUPLEDMODEL_TYPE_NAME, 
        kls=CoupledModel)

def coupledmodels_post(user, coupled_model=None):  # noqa: E501
    """Create one CoupledModel

    Create a new instance of CoupledModel (more information in https://w3id.org/okn/o/sdm#CoupledModel) # noqa: E501

    :param user: Username
    :type user: str
    :param coupled_model: Information about the CoupledModelto be created
    :type coupled_model: dict | bytes

    :rtype: CoupledModel
    """

    if connexion.request.is_json:
        coupled_model = CoupledModel.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(user=user,
        body=coupled_model,
        rdf_type_uri=COUPLEDMODEL_TYPE_URI,
        rdf_type_name=COUPLEDMODEL_TYPE_NAME, 
        kls=CoupledModel)
