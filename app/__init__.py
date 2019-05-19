# from <Package name> import <Class(es) within that Package>
# The lowercase "config" is the name of the Python module 
# config.py, and obviously the one with the uppercase "C" is the actual class.

from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)




from app import routes
