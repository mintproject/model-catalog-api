import connexion
import six

from openapi_server.models.data_set import DataSet  # noqa: E501
from openapi_server import util


def createdataset(data_set):  # noqa: E501
    """Create a dataset

    Creates a new instance of a &#x60;dataset&#x60;. # noqa: E501

    :param data_set: A new &#x60;dataset&#x60; to be created.
    :type data_set: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        data_set = DataSet.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def getdatasets():  # noqa: E501
    """List All datasets

    Gets a list of all &#x60;dataset&#x60; entities. # noqa: E501


    :rtype: List[DataSet]
    """
    return 'do some magic!'
