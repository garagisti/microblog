#from <Package name> import <Class(es) within that Package>
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)




from app import routes
