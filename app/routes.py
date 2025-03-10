# app/routes.py

from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Henrique'}
    posts = [
        {
            'author': {'username' : 'Bruno'},
            'body' : 'Gasolina tá cara'
        },
        {
            'author': {'username' : 'Pedro Maia'},
            'body' : 'Caí da cadeira'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('\login')
def login():
    form = LoginForm
    return render_template('login.html', title='Sign in', form=form)