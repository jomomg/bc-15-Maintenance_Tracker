from flask_wtf import Form
from wtforms import Form, SubmitField, StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired
from models import User, Requests
from flask_login import current_user


#form for first user
class SignUp_form(Form):
	first_name = StringField('First name:', [validators.Length(min= 4,max=25)])
	last_name = StringField('Last name:', [validators.Length(min= 4,max=25)])
	staff_id = StringField('staff_id:'[validators.Length(min=4,max=25)])
	password = PasswordField('New Password:' [validators.DataRequired(),
				validators.Equalto('confirm', message= 'Passwords must match')])
	confirm = PasswordField('Repeat password:', validators=[length(1,120)])
	sign_up = SubmitField('Sign_Up')	

	def validate_staffID(self,field):
		if field.data != self.staff_id and \
		User.query.filter_by(staff_id=field.data).first():
			raise ValidationError('This ID exists')




#signin if account already exists
class SignIn_form(Form):
	email = StringField('Email:', validators=[Required()])
	password = PasswordField('Password:',validators=[Required()])
	sign_in = SubmitField('Sign_In')


class submit_request_form(Form):
	staff_name = StringField('Name:', validators=[Required()])
	staff_id = StringField('StaffID:', validators=[Required()])
	date_of_request = 
	department = StringField('Department:', validators=[Required()])
	description = StringField('Description:', validators=[Required()])
	#status = StringField('Status:', validators=[Required()])
	photo = FileField(validators=[FileRequired])
	submit_request = SubmitField('Submit')

class admin_login_form(Form):
	admin_name = StringField('Admin:', validators=[Required()])
	admin_password =StringField('Name:', validators=[Required()])
	admin_login = SubmitField('Login')

class manage_requests(Form):

