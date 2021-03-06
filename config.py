"""The Config base class contains settings that are common to all configurations; the dif‐
    ferent subclasses define settings that are specific to a configuration. Additional config‐
    urations can be added as needed
"""
import os


class Config:
    SECRET_KEY = os.urandom(24)
    CSRF_ENABLED = False


class DevelopmentConfig:
    DEBUG = True


class TestingConfig:
    TESTING = True
    DEBUG = True


class ProductionConfig:
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}