from flask import Blueprint

req = Blueprint('req', __name__)

from . import views

