from flask import Flask
from .blueprints import blueprint

app = Flask(__name__)

app.register_blueprint(blueprint)
