from lostfound import app, db
from flask import Flask, render_template, send_from_directory
from lostfound.models import Post
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

@app.route('/login')
def login_page():
  return render_template('loginpage.html')

@app.route('/register')
def register_page():
  return render_template('registerpage.html')

@app.route('/addpost')
def addpost_page():
  return render_template('addpost.html')

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



