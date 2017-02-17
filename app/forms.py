from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, TextAreaField, BooleanField, DateTimeField, FileField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo
from flask_wtf.file import FileField, FileRequired
from ..models import User, Requests
from flask_login import current_user


#form for first user
class SignUp_form(FlaskForm):
	first_name = StringField('First name:', validators=[DataRequired()])
	last_name = StringField('Last name:', validators=[DataRequired()])
	email = StringField('email:',validators=[DataRequired(), Email()])
	username = StringField('username', validators=[DataRequired()])
	password = PasswordField('New Password:',validators=[DataRequired(),
				EqualTo('confirm', message= 'Passwords must match')])
	confirm = PasswordField('Confirm Password')
	sign_up = SubmitField('Sign Up')	

	def validate_email(self,field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('Email address already in use')

	def validate_username(self,field):
		if User.query.filter_by(username=field.data).first():
			raise ValidationError('username already is use')




#signin if account already exists
class SignIn_form(FlaskForm):
	email = StringField('email:', validators=[DataRequired(), Email()])
	password = PasswordField('Password:',validators=[DataRequired()])
	sign_in = SubmitField('Sign_In')
'''

class submit_request_form(FlaskForm):
	staff_name = StringField('Name:', validators=[DataRequired()])
	staff_id = StringField('StaffID:', validators=[DataRequired()])
	date_of_request = DateTimeField('Date of Request',validators=[DataRequired()])
	department = StringField('Department:', validators=[DataRequired()])
	description = TextAreaField('Description:', validators=[DataRequired()])
	#status = StringField('Status:', validators=[Required()])
	photo = FileField('Photo:',validators=[FileRequired])
	submit_request = SubmitField('Submit')
	'''
'''
class admin_login_form(FlaskForm):
	admin_name = StringField('Admin:', validators=[DataRequired()])
	admin_password =StringField('Name:', validators=[DataRequired()])
	admin_login = SubmitField('Login')
'''
'''
class manage_requests(FlaskForm):
	status = SelectField('Status:', choices=[('default', 'Default'),('approved', 'Approved'), ('disapproved', 'Disapproved'), ('closed', 'Closed')], validators=[DataRequired()])
	comments = TextAreaField('Comments:', validators=[DataRequired()])
	contact_name = StringField('Contact Name:', validators=[DataRequired()])
	contact_phone = StringField('Contact phone:', validators=[DataRequired()])
	submit = SubmitField('Submit')

'''