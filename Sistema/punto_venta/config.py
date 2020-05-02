import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SECRET_KEY = b'\xd00&(\xc6\x90\x98\xde\xd6\xefM!\x07b/z\xaa\x88\xc0\xe5\x8f\x01\x92\x86'
