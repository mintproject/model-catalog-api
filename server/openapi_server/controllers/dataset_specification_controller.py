import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import DATASETSPECIFICATION_TYPE_NAME, DATASETSPECIFICATION_TYPE_URI

from openapi_server.models.dataset_specification import DatasetSpecification  # noqa: E501
from openapi_server import util

def datasetspecifications_get(username=None, label=None):  # noqa: E501
    """List all DatasetSpecification entities

    Gets a list of all DatasetSpecification entities # noqa: E501

    :param username: Username to query
    :type username: str
    :param label: Filter by label
    :type label: str

    :rtype: List[DatasetSpecification]
    """


    return get_resource(
        username=username,
        label=label,
        rdf_type_uri=DATASETSPECIFICATION_TYPE_URI,
        rdf_type_name=DATASETSPECIFICATION_TYPE_NAME, 
        kls=DatasetSpecification)

def datasetspecifications_id_delete(id, user):  # noqa: E501
    """Delete a DatasetSpecification

    Delete an existing DatasetSpecification # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=DATASETSPECIFICATION_TYPE_URI,
        rdf_type_name=DATASETSPECIFICATION_TYPE_NAME, 
        kls=DatasetSpecification)

def datasetspecifications_id_get(id, username=None):  # noqa: E501
    """Get a DatasetSpecification

    Gets the details of a single instance of a DatasetSpecification # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: DatasetSpecification
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=DATASETSPECIFICATION_TYPE_URI,
        rdf_type_name=DATASETSPECIFICATION_TYPE_NAME, 
        kls=DatasetSpecification)

def datasetspecifications_id_put(id, user, dataset_specification=None):  # noqa: E501
    """Update a DatasetSpecification

    Updates an existing DatasetSpecification # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param dataset_specification: An old DatasetSpecificationto be updated
    :type dataset_specification: dict | bytes

    :rtype: DatasetSpecification
    """

    if connexion.request.is_json:
        dataset_specification = DatasetSpecification.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=dataset_specification,
        rdf_type_uri=DATASETSPECIFICATION_TYPE_URI,
        rdf_type_name=DATASETSPECIFICATION_TYPE_NAME, 
        kls=DatasetSpecification)

def datasetspecifications_post(user, dataset_specification=None):  # noqa: E501
    """Create a DatasetSpecification

    Create a new instance of a DatasetSpecification # noqa: E501

    :param user: Username
    :type user: str
    :param dataset_specification: A new DatasetSpecificationto be created
    :type dataset_specification: dict | bytes

    :rtype: DatasetSpecification
    """

    if connexion.request.is_json:
        dataset_specification = DatasetSpecification.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=dataset_specification,
        rdf_type_uri=DATASETSPECIFICATION_TYPE_URI,
        rdf_type_name=DATASETSPECIFICATION_TYPE_NAME, 
        kls=DatasetSpecification)
