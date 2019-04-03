import connexion
from endpoint.utils import insert_query, prepare_jsonld
from openapi_server.models.data_set import DataSet  # noqa: E501
from openapi_server.static_vars import *

def createdataset(user):  # noqa: E501
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

    return "Bad request", 403, {}

def getdatasets():  # noqa: E501
    """List All datasets

    Gets a list of all &#x60;dataset&#x60; entities. # noqa: E501


    :rtype: List[DataSet]
    """
    return 'do some magic!'
