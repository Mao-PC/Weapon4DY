import os

from redis import Redis

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_db_url(dbInfo):
    db_type = dbInfo["DBTYPE"] or "sqlite"
    driver = dbInfo["DRIVER"] or ""
    user = dbInfo["USER"] or ""
    pwd = dbInfo["PASSWORD"] or ""
    ipaddr = dbInfo["IPADDR"] or ""
    port = dbInfo["PORT"] or ""
    name = dbInfo["NAME"] or ""

    # sqlite:////tmp/TESTING.db
    return "{}+{}://{}:{}@{}:{}/{}".format(db_type, driver, user, pwd, ipaddr, port, name)


def get_redis_url(redisInfo):
    return Redis(redisInfo["HOST"], redisInfo["PORT"], db=redisInfo["DB_NO"])


class Config:
    TESTING = False
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "WEapon"
    SESSION_TYPE = "redis"


class HomeConfig(Config):
    DEBUG = True
    TESTING = True

    dbInfo = {
        "DBTYPE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "123456",
        "IPADDR": "localhost",
        "PORT": "33306",
        "NAME": "weapon"
    }

    SQLALCHEMY_DATABASE_URI = get_db_url(dbInfo)

    redisInfo = {
        "HOST": "localhost",
        "PORT": 63379,
        "DB_NO": 15
    }

    SESSION_REDIS = get_redis_url(redisInfo)


class CompanyConfig(Config):
    DEBUG = True
    TESTING = True
    dbInfo = {
        "DBTYPE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "123456",
        "IPADDR": "192.168.9.154",
        "PORT": "33306",
        "NAME": "weapon"
    }

    SQLALCHEMY_DATABASE_URI = get_db_url(dbInfo)

    redisInfo = {
        "HOST": "192.168.9.154",
        "PORT": 63379,
        "DB_NO": 15
    }

    SESSION_REDIS = get_redis_url(redisInfo)


env = {
    "home": HomeConfig,
    "com": CompanyConfig
}
