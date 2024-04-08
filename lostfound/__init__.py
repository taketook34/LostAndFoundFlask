from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lost-found.db'
db = SQLAlchemy(app)
app.config['UPLOAD_FOLDER'] = 'photos'


from lostfound import routes