from flask_wtf import FlaskForm
import wtforms
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from flask_wtf.file import FileAllowed, FileRequired
from lostfound.models import User, Post
# from wtforms import validators

class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')

    username = wtforms.StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    password1 = wtforms.PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = wtforms.PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = wtforms.SubmitField(label='Create Account')

class PostForm(FlaskForm):
    name = wtforms.StringField(label='Title: ', validators=[Length(min=2, max=30), DataRequired()])
    description = wtforms.TextAreaField(label='Description: ', validators=[Length(min=10), DataRequired()])
    photo = wtforms.FileField(label='Photo: ', validators=[FileAllowed(['jpg', 'jpeg', 'png']), FileRequired()])
    submit = wtforms.SubmitField(label='Post')

class LoginForm(FlaskForm):
    username = wtforms.StringField(label='User Name:')
    password = wtforms.PasswordField(label='Password:')
    submit = wtforms.SubmitField(label='Log in')