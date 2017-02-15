from flask_wtf import Form
from wtforms import Form, SubmitField, StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired
from models import User
from flask_login import current_user


#form for first user
class SignUp_form(Form):
	first_name = StringField('First name:', [validators.Length(min= 4,max=25)])
	last_name = StringField('Last name:', [validators.Length(min= 4,max=25)])
	email = StringField('email:'[validators.Length(min=4,max=25)])
	password = PasswordField('New Password:' [validators.DataRequired(),
				validators.Equalto('confirm', message= 'Passwords must match')])
	confirm = PasswordField('Repeat password:', validators=[length(1,120)])
	sign_up = SubmitField('Sign_Up')	

	def validate_email(self,field):
		if field.data != self.email and \
		User.query.filter_by(email=field.data).first():
			raise ValidationError('This emailaddress exists')




#signin if account already exists
class SignIn_form(Form):
	email = StringField('Email:', validators=[Required()])
	password = PasswordField('Password:',validators=[Required()])
	sign_in = SubmitField('Sign_In')
