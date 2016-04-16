from flask import Flask
app = Flask(__name__, static_url_path='/static', instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
from . import views