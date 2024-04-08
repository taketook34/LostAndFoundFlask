from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lost-found.db'
db = SQLAlchemy(app)
app.config['UPLOAD_FOLDER'] = 'photos'
app.config['SECRET_KEY'] = 'c1f736417795cd0352f0939b11d155d6a5e1154461e61564'


from lostfound import routes