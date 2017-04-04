from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextField
from wtforms.validators import DataRequired
from ..models import Requests


class RequestsForm(FlaskForm):
	"""
	user adds a maintenance request

	"""

	description = TextField('Description', validators=[DataRequired()])
	department = StringField('Department', validators=[DataRequired()])
	date_of_request=StringField('Date', validators=[DataRequired()])
	photo = StringField('Photo', validators=[DataRequired()])
	submit = SubmitField('Submit Request')