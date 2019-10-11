import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import SOFTWAREIMAGE_TYPE_NAME, SOFTWAREIMAGE_TYPE_URI

from openapi_server.models.software_image import SoftwareImage  # noqa: E501
from openapi_server import util

def softwareimages_get(username=None, label=None):  # noqa: E501
    """List all SoftwareImage entities

    Gets a list of all SoftwareImage entities # noqa: E501

    :param username: Username to query
    :type username: str
    :param label: Filter by label
    :type label: str

    :rtype: List[SoftwareImage]
    """


    return get_resource(
        username=username,
        label=label,
        rdf_type_uri=SOFTWAREIMAGE_TYPE_URI,
        rdf_type_name=SOFTWAREIMAGE_TYPE_NAME, 
        kls=SoftwareImage)

def softwareimages_id_delete(id, user):  # noqa: E501
    """Delete a SoftwareImage

    Delete an existing SoftwareImage # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=SOFTWAREIMAGE_TYPE_URI,
        rdf_type_name=SOFTWAREIMAGE_TYPE_NAME, 
        kls=SoftwareImage)

def softwareimages_id_get(id, username=None):  # noqa: E501
    """Get a SoftwareImage

    Gets the details of a single instance of a SoftwareImage # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: SoftwareImage
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=SOFTWAREIMAGE_TYPE_URI,
        rdf_type_name=SOFTWAREIMAGE_TYPE_NAME, 
        kls=SoftwareImage)

def softwareimages_id_put(id, user, software_image=None):  # noqa: E501
    """Update a SoftwareImage

    Updates an existing SoftwareImage # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param software_image: An old SoftwareImageto be updated
    :type software_image: dict | bytes

    :rtype: SoftwareImage
    """

    if connexion.request.is_json:
        software_image = SoftwareImage.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=software_image,
        rdf_type_uri=SOFTWAREIMAGE_TYPE_URI,
        rdf_type_name=SOFTWAREIMAGE_TYPE_NAME, 
        kls=SoftwareImage)

def softwareimages_post(user, software_image=None):  # noqa: E501
    """Create a SoftwareImage

    Create a new instance of a SoftwareImage # noqa: E501

    :param user: Username
    :type user: str
    :param software_image: A new SoftwareImageto be created
    :type software_image: dict | bytes

    :rtype: SoftwareImage
    """

    if connexion.request.is_json:
        software_image = SoftwareImage.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=software_image,
        rdf_type_uri=SOFTWAREIMAGE_TYPE_URI,
        rdf_type_name=SOFTWAREIMAGE_TYPE_NAME, 
        kls=SoftwareImage)
