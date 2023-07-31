"""Main Module"""
import os

from flask import Flask
from dotenv import load_dotenv

from .web import web
from .dashboard import dashboard


load_dotenv()


def create_app(test_config=None):
    """Flask app factory"""
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(web.blueprint)
    app.register_blueprint(dashboard.blueprint)

    return app
