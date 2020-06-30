import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import DEFAULT_TYPE_NAME, DEFAULT_TYPE_URI

from openapi_server.models.user import User  # noqa: E501
from openapi_server import util

def user_login_post(user=None):  # noqa: E501
    """user_login_post

    Login the user # noqa: E501

    :param user: User credentials
    :type user: dict | bytes

    :rtype: str
    """

    if connexion.request.is_json:
        user = User.from_dict(connexion.request.get_json())  # noqa: E501

    return query_manager.post_resource(
        body=user,
        rdf_type_uri=DEFAULT_TYPE_URI,
        rdf_type_name=DEFAULT_TYPE_NAME, 
        kls=Default)
