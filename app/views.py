from flask import flash, render_template, session, redirect, url_for, request, abort
from forms import SignUp_form, SignIn_form, 
from app import app
from models import User
from flask_login import login_user, logout_user
import os

#The Homepage
@app.route('/')
def index():
	return render_template("index.html")

#staff sign in page
@app.route('/user/signin', methods=['GET','POST'])
def sign_in():
	form = SignIn_form()
	if form.validate_on_submit():
		usr = User.query.filter_by(staff_id=form.staff_id.data).first()
		if usr is not None and usr.verify_password(form.password.data):
			login_user(usr, form.remember.data)
			return redirect(request.args.get('next') or url_for('index'))
		flash('Invalid username or password')
	return render_template("sign_in.html", form=form, heading="Sign In")


#Logging out of one's account
@app.route('/signout')
@login_required
def signout():
	logout_user()
	flash('You have been logged out.')
	return redirect(url_for('signin'))

##registering a new account i.e new user
@app.route('/user/signup', methods=['GET', 'POST'])
def sign_up():
	form = SignUp_form()
	if form.validate_on_submit():
		user = User(first_name = form.first_name.data,
					last_name = form.last_name.data,
					staff_id = form.staff_id.data,
					password = form.password.data,
					role = 'default')
		db.session.add(user)
		flash('Thank you for registering')
		return redirect(url_for('signin'))
	return render_template("signup.html", form=form, heading="Sign Up")





@app.route('/user/signin/submitrequest', methods=['GET', 'POST'])
def make_request():
	form = submit_request_form():

@app.route('/user/signin/viewstatus')




@app.route('/user/admin', methods=['GET', 'POST'])
def admin_login():
	form = admin_login_form()
	if form.validate_on_submit():



@app.route('/user/admin/managerequests', methods=['GET','POST'])
def manage_requests():
