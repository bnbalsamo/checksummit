from flask import Flask
from .blueprint import BLUEPRINT

app = Flask(__name__)


#app.config['DISALLOWED_ALGOS'] = ["md5", "crc32"]
#app.config['BUFF'] = 1024*1000*8
app.config.from_envvar('CHECKSUMMIT_CONFIG', silent=True)


app.register_blueprint(BLUEPRINT)
