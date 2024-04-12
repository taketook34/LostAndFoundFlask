from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_admin import Admin


import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lost-found.db'
db = SQLAlchemy(app)
app.config['UPLOAD_FOLDER'] = 'lostfound/static/photos'
app.config['SECRET_KEY'] = 'c1f736417795cd0352f0939b11d155d6a5e1154461e61564'
login_manager = LoginManager(app)

migrate = Migrate(app, db)
admin = Admin(app)


from lostfound import admins
from lostfound import routes