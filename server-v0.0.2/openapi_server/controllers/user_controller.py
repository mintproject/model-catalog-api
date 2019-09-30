import connexion
import six

from openapi_server.models.user import User  # noqa: E501
from werkzeug.exceptions import Unauthorized
import time
from openapi_server.config import db

from jose import JWTError, jwt

JWT_ISSUER = 'com.zalando.connexion'
JWT_SECRET = 'change_this'
JWT_LIFETIME_SECONDS = 60000000
JWT_ALGORITHM = 'HS256'


def decode_token(token):
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except JWTError as e:
        six.raise_from(Unauthorized, e)


def _current_timestamp() -> int:
    return int(time.time())


def create_user():  # noqa: E501
    """Create user

    This can only be done by the logged in user. # noqa: E501

    :param user: Created user object
    :type user: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        user_json = connexion.request.get_json()
        username = user_json['username']
        password = user_json['password']
        try:
            validate_username(username)
        except ValueError as e:
            return "Please use a different username", 403, {}

        p = User(username=user_json['username'])
        p.set_password(password)
        db.session.add(p)
        db.session.commit()

    return "Created", 200, {}


def validate_username(username):
    user = User.query.filter_by(_username=username).first()
    if user is not None:
        raise ValueError('Please use a different username.')


def delete_user(username):  # noqa: E501
    """Delete user

    This can only be done by the logged in user. # noqa: E501

    :param username: The name that needs to be deleted
    :type username: str

    :rtype: None
    """
    return "Not Implemented", 501, {}


def get_user_by_name(username):  # noqa: E501
    """Get user by user name

     # noqa: E501

    :param username: The name that needs to be fetched. Use user1 for testing.
    :type username: str

    :rtype: User
    """
    return "Not Implemented", 501, {}


def login_user(username, password):  # noqa: E501
    """Logs user into the system

     # noqa: E501

    :param username: The user name for login
    :type username: str
    :param password: The password for login in clear text
    :type password: str

    :rtype: str
    """
    user = User.query.filter_by(_username=username).first()
    if user is None or not user.check_password(password):
        return "Invalid User or Password", 401, {}

    timestamp = _current_timestamp()
    payload = {
        "iss": JWT_ISSUER,
        "iat": int(timestamp),
        "exp": int(timestamp + JWT_LIFETIME_SECONDS),
        "sub": str(username),
    }

    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


def logout_user():  # noqa: E501
    """Logs out current logged in user session

     # noqa: E501


    :rtype: None
    """
    return "Not Implemented", 501, {}


def update_user(username, user):  # noqa: E501
    """Updated user

    This can only be done by the logged in user. # noqa: E501

    :param username: name that need to be updated
    :type username: str
    :param user: Updated user object
    :type user: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        user = User.from_dict(connexion.request.get_json())  # noqa: E501
    return "Not Implemented", 501, {}
