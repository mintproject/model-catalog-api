import os
import connexion
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

# Create the connexion application instance
app = connexion.App(__name__, specification_dir='./openapi/')

# Build the Sqlite ULR for SqlAlchemy
sqlite_url = "sqlite:////" + os.path.join(basedir, "database/server.db")

# Configure the SqlAlchemy part of the app instance
app.app.config["SQLALCHEMY_ECHO"] = True
app.app.config["SQLALCHEMY_DATABASE_URI"] = sqlite_url
app.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create the SqlAlchemy db instance
db = SQLAlchemy(app.app)
