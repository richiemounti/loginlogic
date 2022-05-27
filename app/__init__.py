import os
from flask import (
    Flask,
    current_app
)

from flask_session import Session
from flask_login import LoginManager
from config import DevelopmentConfig, Config
from app.extensions import (
    csrf_protect,
    login,
    bcrypt,
    db
)

app = Flask(__name__)

app.secret_key = ("b'\xbc\xe1\xbe_-\xbba\x81u\xd2\x16\xf2\t\xdass'")
app.config.from_object(['DevelopmentConfig'])
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:mulama@localhost:5432/carthagedb"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
bcrypt.init_app(app)
login.init_app(app)
csrf_protect.init_app(app)