"""App Init"""
import os
from flask import Flask
from app.routes import animal
from app.db.config import db, migrate

app = Flask(__name__)

DB_DIALECT = os.getenv('DB_DIALECT')
DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
CONNECTION_STRING = f"{DB_DIALECT}://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
app.config['SQLALCHEMY_DATABASE_URI'] = CONNECTION_STRING
db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(animal.animal_blueprint, url_prefix="/animal")
