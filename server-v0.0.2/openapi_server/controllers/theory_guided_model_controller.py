import connexion
import six

from openapi_server.models.theory_guided_model import TheoryGuidedModel  # noqa: E501
from openapi_server import util


def theory_guidedmodels_get(username=None):  # noqa: E501
    """List all Theory-GuidedModel entities

    Gets a list of all Theory-GuidedModel entities # noqa: E501

    :param username: Username to query
    :type username: str

    :rtype: List[TheoryGuidedModel]
    """
    return 'do some magic!'


def theory_guidedmodels_id_delete(id):  # noqa: E501
    """Delete a Theory-GuidedModel

    Delete an existing Theory-GuidedModel # noqa: E501

    :param id: The ID of the resource
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def theory_guidedmodels_id_get(id, username=None):  # noqa: E501
    """Get a Theory-GuidedModel

    Gets the details of a single instance of a Theory-GuidedModel # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: TheoryGuidedModel
    """
    return 'do some magic!'


def theory_guidedmodels_id_put(id, theory_guided_model=None):  # noqa: E501
    """Update a Theory-GuidedModel

    Updates an existing Theory-GuidedModel # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param theory_guided_model: An old Theory-GuidedModelto be updated
    :type theory_guided_model: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        theory_guided_model = TheoryGuidedModel.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def theory_guidedmodels_post(theory_guided_model=None):  # noqa: E501
    """Create a Theory-GuidedModel

    Create a new instance of a Theory-GuidedModel # noqa: E501

    :param theory_guided_model: A new Theory-GuidedModelto be created
    :type theory_guided_model: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        theory_guided_model = TheoryGuidedModel.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
