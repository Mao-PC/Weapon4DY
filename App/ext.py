from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


def init_model(app):
    db.init_app(app)
    migrate.init_app(app, db)
    Session(app)
