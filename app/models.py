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


@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(int(user_id))
