from flask import Blueprint
from App.models import User

from App.ext import db

mao_test = Blueprint('mao_test', __name__)


@mao_test.route('/')
def index():
    return 'mao_test TEST'


@mao_test.route('/createDB')
def create_db():
    db.create_all()
    return '创建成功'


@mao_test.route('/dropDB')
def drop_all():
    db.drop_all()
    return '删库成功'


@mao_test.route('/addUser')
def add_user():
    user = User()
    user.username = 'TTT'
    db.session.add(user)
    db.session.commit()
    return '用户添加成功'
