import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import IMAGE_TYPE_NAME, IMAGE_TYPE_URI

from openapi_server.models.image import Image  # noqa: E501
from openapi_server import util

def images_get(username=None, label=None):  # noqa: E501
    """List all Image entities

    Gets a list of all Image entities # noqa: E501

    :param username: Username to query
    :type username: str
    :param label: Filter by label
    :type label: str

    :rtype: List[Image]
    """


    return get_resource(
        username=username,
        label=label,
        rdf_type_uri=IMAGE_TYPE_URI,
        rdf_type_name=IMAGE_TYPE_NAME, 
        kls=Image)

def images_id_delete(id, user):  # noqa: E501
    """Delete a Image

    Delete an existing Image # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str

    :rtype: None
    """


    return delete_resource(id=id,user=user,
        rdf_type_uri=IMAGE_TYPE_URI,
        rdf_type_name=IMAGE_TYPE_NAME, 
        kls=Image)

def images_id_get(id, username=None):  # noqa: E501
    """Get a Image

    Gets the details of a single instance of a Image # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param username: Username to query
    :type username: str

    :rtype: Image
    """


    return get_resource(id=id,
        username=username,
        rdf_type_uri=IMAGE_TYPE_URI,
        rdf_type_name=IMAGE_TYPE_NAME, 
        kls=Image)

def images_id_put(id, user, image=None):  # noqa: E501
    """Update a Image

    Updates an existing Image # noqa: E501

    :param id: The ID of the resource
    :type id: str
    :param user: Username
    :type user: str
    :param image: An old Imageto be updated
    :type image: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        image = Image.from_dict(connexion.request.get_json())  # noqa: E501

    return put_resource(id=id,user=user,
        body=image,
        rdf_type_uri=IMAGE_TYPE_URI,
        rdf_type_name=IMAGE_TYPE_NAME, 
        kls=Image)

def images_post(user, image=None):  # noqa: E501
    """Create a Image

    Create a new instance of a Image # noqa: E501

    :param user: Username
    :type user: str
    :param image: A new Imageto be created
    :type image: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        image = Image.from_dict(connexion.request.get_json())  # noqa: E501

    return post_resource(user=user,
        body=image,
        rdf_type_uri=IMAGE_TYPE_URI,
        rdf_type_name=IMAGE_TYPE_NAME, 
        kls=Image)
