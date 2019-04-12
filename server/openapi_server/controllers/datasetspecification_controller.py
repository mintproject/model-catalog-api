import connexion
import six

from openapi_server.models.dataset_specification import DatasetSpecification  # noqa: E501
from openapi_server.models.variable_presentation import VariablePresentation  # noqa: E501
from openapi_server import util
from openapi_server.static_vars import *
from endpoint.utils import insert_query, prepare_jsonld, get_all_resource


def create_data_set(user):  # noqa: E501
    """Create a datasetspecification

    Creates a new instance of a &#x60;datasetspecification&#x60;. # noqa: E501

    :param dataset_specification: A new &#x60;datasetspecification&#x60; to be created.
    :type dataset_specification: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        dataset = DatasetSpecification.from_dict(connexion.request.get_json())  # noqa: E501
        if dataset.type:
            dataset.type.append(DATASETSPECIFICATION_TYPE)
        else:
            dataset.type = [DATASETSPECIFICATION_TYPE]
        dataset_json = prepare_jsonld(dataset, user)
        return insert_query(dataset_json, user)

    return "Bad request", 400, {}



def get_data_sets(username=None):  # noqa: E501
    """List All datasetspecifications

    Gets a list of all &#x60;datasetspecification&#x60; entities. # noqa: E501

    :param username: To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username
    :type username: str

    :rtype: List[DatasetSpecification]
    """
    data = DatasetSpecification()
    try:
        response = get_all_resource(DATASETSPECIFICATION_TYPE, data.openapi_types, username)
    except:
        return "Bad request", 400, {}

    data_sets = []
    for d in response:
        data_sets.append(DatasetSpecification.from_dict(d))

    return data_sets
