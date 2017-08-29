class Config(object):
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    SECRET_KEY = "random secret key"
    DEBUG = True

class TestingConfig(DevelopmentConfig):
    SECRET_KEY = "random secret key for test"
    TESTING = True