import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import FUNDINGINFORMATION_TYPE_NAME, FUNDINGINFORMATION_TYPE_URI

from openapi_server.models.funding_information import FundingInformation  # noqa: E501
from openapi_server import util

def fundinginformations_get(username=None, label=None):  # noqa: E501
    """List all FundingInformation entities

    Gets a list of all FundingInformation entities # noqa: E501

    :param username: Username to query
    :type username: str
    :param label: Filter by label
    :type label: str

    :rtype: List[FundingInformation]
    """


    return get_resource(
        username=username,
        label=label,
        rdf_type_uri=FUNDINGINFORMATION_TYPE_URI,
        rdf_type_name=FUNDINGINFORMATION_TYPE_NAME, 
        kls=FundingInformation)

def fundinginformations_id_delete(id, user):  # noqa: E501
    """Delete a FundingInformation

    Delete an existing FundingInformation # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=FUNDINGINFORMATION_TYPE_URI,
        rdf_type_name=FUNDINGINFORMATION_TYPE_NAME, 
        kls=FundingInformation)

def fundinginformations_id_get(id, username=None):  # noqa: E501
    """Get a FundingInformation

    Gets the details of a single instance of a FundingInformation # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: FundingInformation
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=FUNDINGINFORMATION_TYPE_URI,
        rdf_type_name=FUNDINGINFORMATION_TYPE_NAME, 
        kls=FundingInformation)

def fundinginformations_id_put(id, user, funding_information=None):  # noqa: E501
    """Update a FundingInformation

    Updates an existing FundingInformation # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param funding_information: An old FundingInformationto be updated
    :type funding_information: dict | bytes

    :rtype: FundingInformation
    """

    if connexion.request.is_json:
        funding_information = FundingInformation.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=funding_information,
        rdf_type_uri=FUNDINGINFORMATION_TYPE_URI,
        rdf_type_name=FUNDINGINFORMATION_TYPE_NAME, 
        kls=FundingInformation)

def fundinginformations_post(user, funding_information=None):  # noqa: E501
    """Create a FundingInformation

    Create a new instance of a FundingInformation # noqa: E501

    :param user: Username
    :type user: str
    :param funding_information: A new FundingInformationto be created
    :type funding_information: dict | bytes

    :rtype: FundingInformation
    """

    if connexion.request.is_json:
        funding_information = FundingInformation.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=funding_information,
        rdf_type_uri=FUNDINGINFORMATION_TYPE_URI,
        rdf_type_name=FUNDINGINFORMATION_TYPE_NAME, 
        kls=FundingInformation)
