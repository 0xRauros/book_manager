'''
Application factory
All the external apps are initialized here.
'''
from flask import Flask
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy 
from config import config

moment = Moment()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    moment.init_app(app)
    db.init_app(app)

    return app
