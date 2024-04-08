from lostfound import db
from werkzeug.security import generate_password_hash, check_password_hash

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    description = db.Column(db.String(255))
    # author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # author = db.relationship('User', backref='posts')  # Relationship with User
    photo = db.Column(db.String(255), nullable=True)  # Assuming photo path is stored as string
    date = db.Column(db.DateTime, default=db.func.now())  # Use db.func.now() instead

    def __str__(self):
        return f"{self.id}:{self.name}"


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(60), unique=True, nullable=False)
#     password = db.Column(db.String(120), nullable=False)

#     def set_password(self, password):
#         self.password = generate_password_hash(password)

#     def check_password(self, password):
#         return check_password_hash(self.password, password)