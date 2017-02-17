'''
from flask import flash, render_template, session, redirect, url_for, request, abort
from app.forms import SignUp_form, SignIn_form
from tracker import app
#from app.models import User
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
# @login_required
def signout():
	logout_user()
	flash('You have been logged out.')
	return redirect(url_for('sign_in'))

##registering a new account i.e new user
@app.route('/user/signup', methods=['GET', 'POST'])
def sign_up():
	form = SignUp_form()
	if form.validate_on_submit():
		user = User(first_name = form.first_name.data,
					last_name = form.last_name.data,
					staff_id = form.staff_id.data,
					password = form.password.data,
					confirm = form.confirm.data
					)
		db.session.add(user)
		db.session.commit()
		flash('Thank you for registering')
		return redirect(url_for('make_request'))
	return render_template("sign_up.html", form=form, heading="Sign Up")


@app.route('/user/admin', methods=['GET', 'POST'])
def admin_login():
	form = admin_login_form()
	if request.form['admin_name'] != 'admin' or request.form['admin_password'] != 'admin':
		error = 'Invalid Credentials. Please try again.'
	else:
		return redirect(url_for('manage_requests'))
	#return render_template('login.html', error=error)

@app.route('/user/signin/submitrequest', methods=['GET', 'POST'])
def make_request():
	form = submit_request_form()
	if form.validate_on_submit():
		submit= Requests(staff_id = form.staff_id.data,
			department = form.department.data,
			description = form.description.data,
			date_of_request = form.date_of_request.data,
			photo = form.photo.data
			)
		db.session.add(submit)
		flash('Your request has been received and is being processed')
		return redirect(url_for('index'))



@app.route('/user/signin/viewstatus')
def view_requests():
	requests = Request.query.all()
	return render_template("#", data=requests)



@app.route('/user/admin', methods=['GET', 'POST'])
def admin_login():
	form = admin_login_form()
	error = None
	if request.method == 'POST':
		if request.form['admin_name'] != 'admin' or request.form['admin_password'] != 'admin':
			error = 'Invalid Credentials. Please try again.'
		else:
			return redirect(url_for('manage_requests'))
	
	return render_template('login.html', error=error)
 




@app.route('/user/admin/managerequests', methods=['GET','POST'])
def manage_requests():
	form = 
'''

'''