import six
from jose import JWTError, jwt
import time
import json
import requests
from werkzeug.exceptions import Unauthorized

from openapi_server.settings import AUTH_SERVER, AUTH_CLIENT_ID, AUTH_SECRET, JWT_ALGORITHM

def decode_token(token):
    try:
        return jwt.decode(token, AUTH_SECRET)
    except JWTError as e:
        six.raise_from(Unauthorized, e)


def _current_timestamp() -> int:
    return int(time.time())


def auth_with_password(email, password):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
 
    data =   {
            "username": email,
            "password": password,
            "grant_type": "password",
            "client_id": AUTH_CLIENT_ID
        }
    print(AUTH_SERVER)
    response = requests.post(
        AUTH_SERVER,
        headers=headers,
        data=data)

    return response


def user_login_get(username, password):  # noqa: E501
    """Logs user into the system

     # noqa: E501

    :param username: The user name for login
    :type username: str
    :param password: The password for login in clear text
    :type password: str

    :rtype: str
    """
    response = auth_with_password(username, password)
    if not response.ok:
        return "Invalid User or Password", 401, {}
    return response.text
