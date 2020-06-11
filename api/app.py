from flask import Flask
import os, json, click
from flask_restful import Api

from database.db import initialize_db
from resources.routes import initialize_routes
print(os.environ['HOME'])
class Config():
    if(os.environ.get('MYSQL') is None):
        SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    else:
        SQLALCHEMY_DATABASE_URI = os.environ['MYSQL']

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SECRET_KEY = os.urandom(24)

app = Flask(__name__)
app.config.from_object(Config)

api = Api(app, prefix="/api/v1")
print("Database: " + app.config['SQLALCHEMY_DATABASE_URI'])

initialize_db(app)
initialize_routes(api)
if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1', port=6000)