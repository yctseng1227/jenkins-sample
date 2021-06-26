from flask import Flask
from macacahub.settings import ProdConfig
from macacahub import commands, page


def create_app(config_object=ProdConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_blueprints(app)
    register_commands(app)
    return app


def register_blueprints(app):
    app.register_blueprint(page.views.blueprint)


def register_commands(app):
    app.cli.add_command(commands.test)
