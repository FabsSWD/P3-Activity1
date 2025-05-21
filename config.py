import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'biblioteca_super_secreta'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_DIR, "db", "biblioteca.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
