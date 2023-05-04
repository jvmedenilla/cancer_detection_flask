
from flask import Flask
from config import Config
from flask_restplus import Api

api = Api()

app = Flask(__name__) # special variable to identify current module thats being passed to Flask
app.config.from_object(Config)

api.init_app(app)

from application import app



