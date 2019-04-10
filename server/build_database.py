import os
from openapi_server.config import db
from openapi_server.models import User

# Data to initialize database with
USERS = [
    {'username': 'guest', 'password': 'A9vZusYGJsRsbx9XKKfO'}
]

# Delete database file if it exists currently
if os.path.exists('database/server.db'):
    os.remove('database/server.db')

# Create the database
db.create_all()

# Iterate over the PEOPLE structure and populate the database
for person in USERS:
    p = User(username=person['username'], password=person['password'])
    db.session.add(p)

db.session.commit()
