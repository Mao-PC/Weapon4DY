from flask import Flask

from views.hello import mao_test


def create_app():
    app = Flask(__name__)
    app.register_blueprint(mao_test)
    return app
