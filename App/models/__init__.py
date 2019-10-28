from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_model(app):
    db.init_app(app)