from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from .forms import LoginForm, Registration, RequestsForm
from .. import db
from ..models import User

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = Registration()
    if form.validate_on_submit():
        user = User(
                            
                            first_name=form.first_name.data,
                            last_name=form.last_name.data,
                            email=form.email.data,
                            username=form.username.data,
                            password=form.password.data)

    
        db.session.add(user)
        db.session.commit()
        flash('You have successfully registered! You may now login.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form, title='Register')

#if employee is admin login view redirects
#to admin dashboard

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(
                form.password.data):
            login_user(user)
            if user.is_admin:
                return redirect(url_for('home.admin_dashboard'))
            else:
                return redirect(url_for('home.dashboard'))
        else:
            flash('Invalid email or password.')
    return render_template('auth/login.html', form=form, title='Login')


@app.route('/login/submitrequest', methods=['GET', 'POST'])
@login_required
def make_request():
    form = submit_request_form()
    if form.validate_on_submit():
        submit= Requests(staff_id = form.staff_id.data,
            department = form.department.data,
            description = form.description.data,
            photo = form.photo.data
            )
        db.session.add(submit)
        db.session.commit()
        flash('Your request has been received and is being processed')
        return redirect(url_for('index'))
    return render_template('auth/submit.html', form=form, title='SUbmit request')




@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('auth.login'))