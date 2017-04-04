from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import req
from .forms import RequestsForm
from .. import db
from ..models import *



@req.route('/submitrequest', methods=['GET','POST'])
@login_required
def submitrequest():
	form = RequestsForm()
	if form.validate_on_submit():
		user = current_user.id
		new_request = Requests(description=form.description.data,
								department=form.department.data,
								date_of_request=form.date_of_request.data,
								photo=form.photo.data
								)
		db.session.add(new_request)
		db.session.commit()
		flash('Your request has been received and is being processed.')
		return redirect(url_for('home.dashboard'))
	return render_template('req/submitrequest.html', form=form, title='Submit Request')



@req.route('/myrequests', methods=['GET','POST'])
@login_required
def viewrequests():

	#user = User.query.filter_by(id=current_user.id).first()
	#all_requests = Requests.query.all()
	all_requests = Requests.query.filter_by(id=current_user.id).first()
	
	return render_template('req/myrequests.html', my_requests=all_requests)



