import os

class Config(object):
    DEBUG = True
    TESTING = True
    ENV = "development"
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


class ProductionConfig(Config):
    DEBUG = False
    FLASK_DEBUG = 0
    TESTING = False
    ENV = "production"


class DevelopmentConfig(Config):
    ENV = "development"
    FLASK_DEBUG = 1
    DEVELOPMENT = True
