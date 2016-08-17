from flask import Flask
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from config import config


moment=Moment()
db=SQLAlchemy()


def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    moment.init_app(app)
    db.init_app(app)
    with app.test_request_context():
        from .models import Event
        db.create_all()
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app