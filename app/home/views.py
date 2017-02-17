from flask import render_template
from flask_login import login_required

from . import home

@home.route('/')
def homepage():
	'''
	Render homepage tempplate on the /route
	'''
	return render_template ('home/index.html', title = "Welcome")

@home.route('/dashboard')
@login_required
def dashboard():
	'''
	Render dashboard template on /dashboard route
	'''
	return render_template('home/dashboard.html', title="Dashboard")
