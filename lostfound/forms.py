from flask_wtf import FlaskForm
import wtforms
# from wtforms import validators

class RegisterForm(FlaskForm):
    username = wtforms.StringField(label='User Name:')
    password1 = wtforms.PasswordField(label='Password:')
    password2 = wtforms.PasswordField(label='Confirm Password:')
    submit = wtforms.SubmitField(label='Create Account')

class PostForm(FlaskForm):
    name = wtforms.StringField(label='Title: ')
    description = wtforms.TextAreaField(label='Description: ')
    photo = wtforms.FileField(label='Photo: ')
    submit = wtforms.SubmitField(label='Create Account')