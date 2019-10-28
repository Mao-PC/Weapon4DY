from flask import Blueprint

mao_test = Blueprint('mao_test', __name__)

@mao_test.route('/')
def index():
    return 'mao_test TEST'