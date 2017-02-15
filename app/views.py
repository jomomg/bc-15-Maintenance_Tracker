from flask import flash, render_template, session, redirect, url_for, request, abort
from forms import SignUp_form, SignIn_form
from app import app
from models import User
from flask_login import login_user, logout_user
import os






@app.route('/user/signin', methods=['GET','POST'])
def sign_in():
	form = SignIn_form()
	if form.validate_on_submit():
		usr = User.query.filter_by(email=form.email.data).first()
		if usr is not None and usr.verify_password(form.password.data):
			login_user(usr, form.remember.data)
			#send_sms('+254728696810', 'You just logged in!')
			return redirect(request.args.get('next') or url_for('index'))
		flash('Invalid username or password')
return render_template("signin.html", form=form)



@app.route('/signout')
@login_required
def signout():
	logout_user()
	flash('You have been logged out.')
	return redirect(url_for('signin'))

@app.route('/user/signup', methods=['GET', 'POST'])
def sign_up():
	form = SignUp_form()
	if form.validate_on_submit():
		user = User(first_name = form.first_name.data,
					last_name = form.last_name.data,
					email = form.email.data,
					password = form.password.data,
					role = 'default')
		db.session.add(user)
		flash('You may now Sign In')
		return redirect(url_for('signin'))
return render_template("signup.html", form=form, heading="Sign Up")