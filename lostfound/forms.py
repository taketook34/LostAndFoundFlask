from flask_wtf import FLaskForm
import wtforms 

class RegisterForm(FLaskForm):
    username = wtforms.StringField(label='User Name:')
    password1 = wtforms.PasswordField(label='Password:')
    password2 = wtforms.PasswordField(label='Confirm Password:')
    submit = wtforms.SubmitField(label='Create Account')