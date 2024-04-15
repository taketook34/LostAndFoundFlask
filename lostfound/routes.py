from lostfound import app, db

from flask import Flask, render_template, send_from_directory, redirect, url_for, flash, make_response
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename

from lostfound.models import Post, User, FeedbackMessage
from lostfound.forms import RegisterForm, PostForm, LoginForm, FeedbackMessageForm
import os


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('homepage.html')

@app.route('/postlist')
def postlist_page():
  
  with app.app_context():
    posts = Post.query.all()

  return render_template('postlist.html', items=posts)


@app.route('/postlist/<post_id>')
def onepost_page(post_id):
  with app.app_context():
    post_to_show = Post.query.filter_by(id=post_id).first()
  
  return render_template('showpost.html', post=post_to_show)



@app.route('/register', methods=['GET', 'POST'])
def register_page():
  form = RegisterForm()

  if form.validate_on_submit():
    with app.app_context():
      user_to_create = User(username=form.username.data, password=form.password1.data)
      user_to_create.set_password(user_to_create.password)

      db.session.add(user_to_create)
      db.session.commit()
      login_user(user_to_create)

    #set cookie
    response = make_response(redirect(url_for('home_page')))
    response.set_cookie('username', current_user.username)
    response.set_cookie('logged_in', 'True')

    return response

    #return redirect(url_for('home_page'))


  if form.errors != {}: #If there are not errors from the validations
    for err_msg in form.errors.values():
      print(f'There was an error with creating a user: {err_msg}')

  return render_template('registerpage.html', form = form)

@app.route('/addpost', methods=['GET', 'POST'])
@login_required
def addpost_page():
  form  = PostForm()
  
  if current_user.is_authenticated:
    if form.validate_on_submit():
      if form.photo.data:
        filename = secure_filename(form.photo.data.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        form.photo.data.save(filepath)

      with app.app_context():
        post_to_create = Post(name=form.name.data,
          description=form.description.data,
          author_id=current_user.id,
          photo=filename)
        
        db.session.add(post_to_create)
        db.session.commit()

  else:
    flash('User are not authenticated! Please try again', category='danger')

  # MAke post creating after login 

  return render_template('addpost.html', form = form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
  form = LoginForm()

  if form.validate_on_submit():
    attempted_user = User.query.filter_by(username=form.username.data).first()

    if attempted_user and attempted_user.check_password(form.password.data):
        login_user(attempted_user)
        flash(f'Success! You are logged in as: {attempted_user.username}', category='success')

        #Set cookie for site
        response = make_response(redirect(url_for('home_page')))
        response.set_cookie('username', current_user.username)
        response.set_cookie('logged_in', 'True')

        return response

        # return redirect(url_for('home_page'))
    else:
        flash('Username and password are not match! Please try again', category='danger')

  return render_template('loginpage.html', form=form)

@app.route('/logout')
@login_required
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')

    #Delete cookie
    response = make_response(redirect(url_for("home_page")))
    response.delete_cookie('username')
    response.delete_cookie('logged_in')

    return response

    # return redirect(url_for("home_page"))

@app.route('/contacts', methods=['GET', 'POST'])
def contacts_page():

  form = FeedbackMessageForm()

  if form.validate_on_submit():
    email = form.email.data
    text = form.text.data

    # Сохранение сообщения в БД
    new_message = FeedbackMessage(email=email, text=text)
    db.session.add(new_message)
    db.session.commit()
    

  context = {
        "authors": [
            {"name":"Хусаінов Дмитро ІО-11"},
            {"name":"Шинкарчук Богдан ІО-11"},
            {"name":"Столярчук Микола ІО-11"}
        ],
        'page_title': 'Про нас',

    }
  return render_template('contacts.html', data=context, form=form)



