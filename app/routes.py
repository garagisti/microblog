from flask import render_template, flash, redirect
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

@app.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(form.username.data,form.remember_me.data))
		return redirect(url_for('index'))
	return render_template('login.html', title='Sign In', form=form)