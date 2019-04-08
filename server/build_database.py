import os
from openapi_server.config import db

# Delete database file if it exists currently
if os.path.exists('server.db'):
    os.remove('server.db')

# Create the database
db.create_all()

db.session.commit()
