from flask import Flask

from App.cfg import env
from App.ext import init_model
from App.routers import shows


def create_app(cenv):
    app = Flask(__name__)
    # 注册路由
    app.register_blueprint(shows)
    # 注册model
    app.config.from_object(env[cenv])
    init_model(app)
    return app
