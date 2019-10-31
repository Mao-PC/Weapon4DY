from flask import Blueprint, request, session

from App.ext import db
from App.models import User

shows = Blueprint('mao_test', __name__)


@shows.route('/ip')
def index():
    return request.remote_addr


@shows.route('/createDB')
def create_db():
    db.create_all()
    return '创建成功'


@shows.route('/dropDB')
def drop_all():
    db.drop_all()
    return '删库成功'


@shows.route('/addUser')
def add_user():
    user = User()
    user.username = 'TTT'
    db.session.add(user)
    db.session.commit()
    return '用户添加成功'


@shows.route('/addse')
def add_se():
    session['name'] = 'mao'
    return 'o的k'
