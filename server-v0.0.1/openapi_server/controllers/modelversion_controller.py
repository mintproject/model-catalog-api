import connexion
import six

from openapi_server.models.model_version import ModelVersion  # noqa: E501
from openapi_server import util


def create_model_version(model_version):  # noqa: E501
    """Create a ModelVersion

    Creates a new instance of a &#x60;ModelVersion&#x60;. # noqa: E501

    :param model_version: A new &#x60;ModelVersion&#x60; to be created.
    :type model_version: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        model_version = ModelVersion.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_model_version(model_version_id):  # noqa: E501
    """Delete a ModelVersion

    Deletes an existing &#x60;ModelVersion&#x60;. # noqa: E501

    :param model_version_id: A unique identifier for a &#x60;ModelVersion&#x60;.
    :type model_version_id: str

    :rtype: None
    """
    return 'do some magic!'


def get_model_version(model_version_id):  # noqa: E501
    """Get a ModelVersion

    Gets the details of a single instance of a &#x60;ModelVersion&#x60;. # noqa: E501

    :param model_version_id: A unique identifier for a &#x60;ModelVersion&#x60;.
    :type model_version_id: str

    :rtype: ModelVersion
    """
    return 'do some magic!'


def get_model_versions():  # noqa: E501
    """List All ModelVersions

    Gets a list of all &#x60;ModelVersion&#x60; entities. # noqa: E501


    :rtype: List[ModelVersion]
    """
    return 'do some magic!'


def update_model_version(model_version_id, model_version):  # noqa: E501
    """Update a ModelVersion

    Updates an existing &#x60;ModelVersion&#x60;. # noqa: E501

    :param model_version_id: A unique identifier for a &#x60;ModelVersion&#x60;.
    :type model_version_id: str
    :param model_version: Updated &#x60;ModelVersion&#x60; information.
    :type model_version: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        model_version = ModelVersion.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
