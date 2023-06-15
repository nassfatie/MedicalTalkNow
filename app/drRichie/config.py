import os
from decouple import config

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class Settings:
    SECRET_KEY = config('SECRET_KEY', 'secret')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevSetting(Settings):
    DEBUG = config('DEBUG')
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'richie.db')

class TestSetting(Settings):
    pass

class ProdSetting(Settings):
    pass

conf_dict = {
    'dev':DevSetting,
    'test':TestSetting,
    'prod':ProdSetting
}