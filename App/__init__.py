from flask import Flask

from App.models import init_model
from App.routers import mao_test

def create_app():
    app = Flask(__name__)
    # 注册路由
    app.register_blueprint(mao_test)

    # 注册model
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    init_model(app=app)

    return app
