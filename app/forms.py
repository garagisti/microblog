#from <Package name> import <Class(es) within that Package>
from flask_wtf import Flask
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

Class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')

