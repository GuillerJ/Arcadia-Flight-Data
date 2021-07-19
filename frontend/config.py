import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '\x8c\xf0!\x07%Qev\xca\x12\xa15l\x1e>\x1a'
    #FLASK_ENV='development'
    #TESTING=True
    # BBDD
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'bbdd.db3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Envio de errores por Mail
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['guillerjps@hotmail.com']


class ProductionConfig(Config):
    """Uses production database server."""
    DB_SERVER = '192.168.19.32'

class DevelopmentConfig(Config):
    DB_SERVER = 'localhost'
    DEBUG = True

class TestingConfig(Config):
    TESTING = True