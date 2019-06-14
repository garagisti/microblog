# from <Package name> import <Class(es) within that Package>
# The lowercase "config" is the name of the Python module
# config.py, and obviously the one with the uppercase "C" is the actual class.

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

from app import routes, models
