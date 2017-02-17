from flask import Flask
from .blueprint import BLUEPRINT

app = Flask(__name__)

app.register_blueprint(BLUEPRINT)
