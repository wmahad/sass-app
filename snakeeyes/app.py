from flask import Flask
from snakeeyes.blueprints.page import page

def create_app(settings_overide=None):
    """
    create a flask app using the app factory pattern.
    :return add
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    if settings_overide:
        app.config.update(settings_overide)

    app.register_blueprint(page)

    return app