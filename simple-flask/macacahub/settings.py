class ProdConfig:
    ENV = "prod"
    DEBUG = False


class DevConfig:
    ENV = "dev"
    DEBUG = True


class TestConfig:
    TESTING = True
    DEBUG = True
