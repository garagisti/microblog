from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')

def index():
	user = {'user' : 'Rahul'}
	posts = [				
				{
					'author' : {'user': 'Michael'},
					'body'	: 'What kind of race was that?!'
				},
				{
					'author' : {'user': 'Daniel'},
					'body'	: 'Works 8 times out of 10 every time!'
				},
				{
					'author' : {'user': 'Charles'},
					'body'	: 'It was a very frustrating race!!'
				}]
	return render_template('index.html', title='Hola', user = user, posts=posts)

@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', title='Sign In', form=form)