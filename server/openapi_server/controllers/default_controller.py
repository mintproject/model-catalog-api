import connexion
import six
from openapi_server.utils.request import get_resource, get_all_resource, put_resource, post_resource, delete_resource
from openapi_server.utils.vars import DEFAULT_TYPE_NAME, DEFAULT_TYPE_URI

from openapi_server import util

def user_login_get(username, password):  # noqa: E501
    """user_login_get

    Login the user # noqa: E501

    :param username: The user name for login
    :type username: str
    :param password: The password for login in clear text
    :type password: str

    :rtype: str
    """


    return get_resource(
        username=username,
        password=password,
        rdf_type_uri=DEFAULT_TYPE_URI,
        rdf_type_name=DEFAULT_TYPE_NAME, 
        kls=Default)
