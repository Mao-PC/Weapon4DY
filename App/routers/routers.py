from flask import Blueprint

from App.models import db

mao_test = Blueprint('mao_test', __name__)

@mao_test.route('/')
def index():
    return 'mao_test TEST'

@mao_test.route('/createDB')
def create_db():
    db.create_all()
    return '创建成功'