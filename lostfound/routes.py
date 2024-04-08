from lostfound import app, db
from flask import Flask, render_template, send_from_directory, redirect, url_for
from lostfound.models import Post, User
from lostfound.forms import RegisterForm, PostForm
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



@app.route('/register', methods=['GET', 'POST'])
def register_page():
  form = RegisterForm()

  if form.validate_on_submit():
    with app.app_context():
      user_to_create = User(username=form.username.data, password=form.password1.data)
      user_to_create.set_password(user_to_create.password)

      db.session.add(user_to_create)
      db.session.commit()

    return redirect(url_for('home_page'))


  if form.errors != {}: #If there are not errors from the validations
    for err_msg in form.errors.values():
      print(f'There was an error with creating a user: {err_msg}')

  return render_template('registerpage.html', form = form)

@app.route('/addpost')
def addpost_page():
  form  = PostForm()


  return render_template('addpost.html', form = form)

@app.route('/login')
def login_page():
  return render_template('loginpage.html')

@app.route('/contacts')
def contacts_page():

  context = {
        "authors": [
            {"name":"Хусаінов Дмитро ІО-11"},
            {"name":"Шинкарчук Богдан ІО-11"},
            {"name":"Столярчук Микола ІО-11"}
        ],
        'page_title': 'Про нас',

    }
  return render_template('contacts.html', data=context)



