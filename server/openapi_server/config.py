import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from configparser import ConfigParser

# Setting headers to use access_token for the GitHub API
config_fallbacks = {
    'github_access_token': '',
}
config = ConfigParser(config_fallbacks)
config.add_section('database')
config.read('config.ini')

DATABASE_USERNAME = config.get('database', 'username')
DATABASE_PASSWORD = config.get('database', 'password')
DATABASE_HOST = config.get('database', 'host')
DATABASE_PORT = config.get('database', 'port')
DATABASE_NAME = config.get('database', 'name')


# Create the connexion application instance
app = connexion.App(__name__, specification_dir='./openapi/')

# Build the Sqlite ULR for SqlAlchemy
mysql_url = "mysql://{}:{}@{}:{}/{}".format(DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_PORT, DATABASE_NAME)
# Configure the SqlAlchemy part of the app instance
app.app.config["SQLALCHEMY_ECHO"] = True
app.app.config["SQLALCHEMY_DATABASE_URI"] = mysql_url
app.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create the SqlAlchemy db instance
db = SQLAlchemy(app.app)
