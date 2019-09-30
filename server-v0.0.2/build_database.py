import os
from openapi_server.config import db
from openapi_server.models import User

# Data to initialize database with
USERS = [
    {'username': 'guest', 'password': 'A9vZusYGJsRsbx9XKKfO'}
]


# Create the database
db.create_all()

# Iterate over the PEOPLE structure and populate the database
for person in USERS:
    p = User(username=person['username'])
    p.set_password(person['password'])
    db.session.add(p)

db.session.commit()
