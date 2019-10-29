import os

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


class HomeConfig:
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
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class CompanyConfig:
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
    SQLALCHEMY_TRACK_MODIFICATIONS = False


env = {
    "home": HomeConfig,
    "com": CompanyConfig
}