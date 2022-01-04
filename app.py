"""
This file have the configurations
for the server.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes_server.houses import houses
from utils.db import db
from config import SQLITE_PATH

# creating
app = Flask(__name__)
# settings
app.config['SQLALCHEMY_DATABASE_URI'] = SQLITE_PATH
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'mysecretkey'

SQLAlchemy(app)


# routes
app.register_blueprint(houses)