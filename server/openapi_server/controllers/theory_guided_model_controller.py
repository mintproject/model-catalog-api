import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import THEORYGUIDEDMODEL_TYPE_NAME, THEORYGUIDEDMODEL_TYPE_URI

from openapi_server.models.theory_guided_model import TheoryGuidedModel  # noqa: E501
from openapi_server import util

def theory_guidedmodels_get(username=None, label=None):  # noqa: E501
    """List all Theory-GuidedModel entities

    Gets a list of all Theory-GuidedModel entities # noqa: E501

    :param username: Username to query
    :type username: str
    :param label: Filter by label
    :type label: str

    :rtype: List[TheoryGuidedModel]
    """


    return get_resource(
        username=username,
        label=label,
        rdf_type_uri=THEORYGUIDEDMODEL_TYPE_URI,
        rdf_type_name=THEORYGUIDEDMODEL_TYPE_NAME, 
        kls=TheoryGuidedModel)

def theory_guidedmodels_id_delete(id, user):  # noqa: E501
    """Delete a Theory-GuidedModel

    Delete an existing Theory-GuidedModel # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=THEORYGUIDEDMODEL_TYPE_URI,
        rdf_type_name=THEORYGUIDEDMODEL_TYPE_NAME, 
        kls=TheoryGuidedModel)

def theory_guidedmodels_id_get(id, username=None):  # noqa: E501
    """Get a Theory-GuidedModel

    Gets the details of a single instance of a Theory-GuidedModel # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: TheoryGuidedModel
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=THEORYGUIDEDMODEL_TYPE_URI,
        rdf_type_name=THEORYGUIDEDMODEL_TYPE_NAME, 
        kls=TheoryGuidedModel)

def theory_guidedmodels_id_put(id, user, theory_guided_model=None):  # noqa: E501
    """Update a Theory-GuidedModel

    Updates an existing Theory-GuidedModel # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param theory_guided_model: An old Theory-GuidedModelto be updated
    :type theory_guided_model: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        theory_guided_model = TheoryGuidedModel.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=theory_guided_model,
        rdf_type_uri=THEORYGUIDEDMODEL_TYPE_URI,
        rdf_type_name=THEORYGUIDEDMODEL_TYPE_NAME, 
        kls=TheoryGuidedModel)

def theory_guidedmodels_post(user, theory_guided_model=None):  # noqa: E501
    """Create a Theory-GuidedModel

    Create a new instance of a Theory-GuidedModel # noqa: E501

    :param user: Username
    :type user: str
    :param theory_guided_model: A new Theory-GuidedModelto be created
    :type theory_guided_model: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        theory_guided_model = TheoryGuidedModel.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=theory_guided_model,
        rdf_type_uri=THEORYGUIDEDMODEL_TYPE_URI,
        rdf_type_name=THEORYGUIDEDMODEL_TYPE_NAME, 
        kls=TheoryGuidedModel)
