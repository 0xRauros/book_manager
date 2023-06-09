import os


basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'optimusprimeesmiidolo'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # add more...


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL')or'sqlite:///'+os.path.join(
        basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    # sqlite:// is a default <in memory> volatil database.
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL')or'sqlite://'


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')or'sqlite:///'+os.path.join(
        basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

