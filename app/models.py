from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager
from datetime import datetime


class User(UserMixin, db.Model):  #user table
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(64), unique=False)
	last_name = db.Column(db.String(64), unique=False)
	email = db.Column(db.String(64), unique=True)
	username = db.Column(db.String(64))
	password_hash = db.Column(db.String(128))
	is_admin = db.Column(db.Boolean, default=False)

	#requests = db.relationship('Request', backref='user', lazy='dynamic')

	@property 
	def password(self):
		raise AttributeError('password is not a readable attribute')

	@password.setter
	#password set to hashed password
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

	def __repr__(self):
		return '<User %r>' % self.first_name

#user loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Requests(db.Model):
	__tablename__ = 'requests'
	id = db.Column(db.Integer, primary_key=True)
	staff_name = db.Column(db.String(64), unique=False)
	staff_id = db.Column(db.String(200), unique=False)
	description = db.Column(db.String(200), unique=False)
	department = db.Column(db.String(200), unique=False)
	date_of_request = db.Column(db.Date, default=datetime.utcnow)
	status = db.Column(db.String(64), unique=False, default='default')
	admin_comments = db.Column(db.String(200), unique=False)
	assignee_name = db.Column(db.String(64), unique=False)
	assignee_phone_number = db.Column(db.String(64), unique=False)
	date_assigned = db.Column(db.Date)
	photo = db.Column(db.String(64), unique=False)

 

	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	user_requests = db.relationship('User', foreign_keys=[user_id], backref='user')
	



	def __repr__(self):
		return '<Requests %r>' % self.staff_name
