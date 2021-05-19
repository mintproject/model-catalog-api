import json
import requests
from werkzeug.exceptions import Unauthorized
import connexion
from openapi_server.models.user import User
from openapi_server.settings import AUTH_SERVER, AUTH_CLIENT_ID

def decode_token(token):
    pass

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
    
    response = requests.post(
        AUTH_SERVER,
        headers=headers,
        data=data)

    return response


def user_login_post():  # noqa: E501
    """Logs user into the system

     # noqa: E501

    :param username: The user name for login
    :type username: str
    :param password: The password for login in clear text
    :type password: str

    :rtype: str
    """
    if connexion.request.is_json:
        user = User.from_dict(connexion.request.get_json())  # noqa: E501

    response = auth_with_password(user.username, user.password)
    print(response)
    if not response.ok:
        return "Invalid User or Password", 401, {}
    return json.loads(response.text)
