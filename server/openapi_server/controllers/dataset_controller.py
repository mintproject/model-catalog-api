import connexion
from endpoint.utils import insert_query, prepare_jsonld, get_all_resource
from openapi_server.models.data_set import DataSet  # noqa: E501
from openapi_server.static_vars import *



def create_data_set(user):  # noqa: E501
    """Create a dataset

    Creates a new instance of a &#x60;dataset&#x60;. # noqa: E501

    :param data_set: A new &#x60;dataset&#x60; to be created.
    :type data_set: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        _ = DataSet.from_dict(connexion.request.get_json())  # noqa: E501
        dataset_json = prepare_jsonld(connexion.request.get_json(), user, DATASET_TYPE)
        return insert_query(dataset_json, user)

    return "Bad request", 400, {}


def get_data_sets(username=None):  # noqa: E501
    """List All datasets

    Gets a list of all &#x60;dataset&#x60; entities. # noqa: E501

    :param username: To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username
    :type username: str

    :rtype: List[DataSet]
    """
    response = get_all_resource(DATASETSPECIFICATION_TYPE, username)
    try:
        return response.json()
    except:
        return "Bad request", 400, {}
