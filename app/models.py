#import db

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app import db, login_manager

class User(UserMixin, db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(64), unique=False)
	last_name = db.Column(db.String(64), unique=False)
	email = db.Column(db.String(64), unique=True, index=True)
	password_hash = db.Column(db.String(120), unique=False)
	confirmed = db.Column(db.Boolean, default=False)
	role = db.Column(db.String(64), unique=False)
	#is_active = db.Column(db.Boolean, default=True)
	is_admin = db.Column(db.Boolean, default=False)

	requests = db.relationship('Request', backref='user', lazy='dynamic')

	@property 
	def password(self):
		raise AttributeError('password is not a readable attribute')

	@password.setter
	#password set to hashed password
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)
	"""
	def get_id(self):
		return self.id
	"""

	def __repr__(self):
		return '<User %r>' % self.first_name

class Requests(db.Model):
	__tablename__ = 'requests'
	id = db.Column(db.Integer, primary_key=True)
	staff_name = db.Column(db.String(64), unique=False)
	staff_id = db.Column(db.String(200), unique=False)
	description = db.Column(db.String(200), unique=False)
	department = db.Column(db.String(200), unique=False)
	date_of_request = 
	status = db.Column(db.String(64), unique=False, default='default')
	facility_id = db.Column(db.Integer, db.ForeignKey('facilities.id'))#db.ForeignKey('facilities.id')
	admin_comments = db.Column(db.String(200), unique=False)
	assignee_name = db.Column(db.String(64), unique=False)
	assignee_phone_number = db.Column(db.String(64), unique=False)
	date_assigned = db.Column(db.String(64), unique=False)
	photo = db.Column(db.String(64), unique=False)
	#user_id = db.Column(db.Integer, unique=False)
	admin_id = db.Column(db.Integer, unique=False)
 

	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	#admin_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	user_requests = db.relationship('User', foreign_keys=[user_id], backref='user')
	#admin_requests = db.relationship('User', foreign_keys=[admin_id], backref='admin')




	def __repr__(self):
		return '<Request %r>' % self.name

@login_manager.user_loader
def load_user(user_id):
return User.query.get(int(user_id))d =
