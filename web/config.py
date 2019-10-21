import os


class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URI')
    TESTING=os.environ.get('TESTING')
    DEBUG=os.environ.get('DEBUG')

class DevConfig(Config):
    DEBUG=True
    


class TestConfig(Config):
    DEBUG=True

class ProdConfig(Config):
    DEBUG=False

