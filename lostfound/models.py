from lostfound import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    # UserMIxin need for providing methods for login such as self.is_active()
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    posts_list = db.relationship('Post', backref="author_user", lazy=True)


    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"{self.id}:{self.username}:"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    description = db.Column(db.String(255))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True) # id from User model
    photo = db.Column(db.String(255), nullable=True)  
    date = db.Column(db.DateTime, default=db.func.now())  


    def __repr__(self):
        return f"{self.id}:{self.name}:{self.photo}"


