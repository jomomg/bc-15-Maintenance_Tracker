from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import app_config

#initialize the app
#app = Flask(__name__, instance_relative_config=True)

#Load the views
#from app import views

#load config file
app.config.from_object('config')

db = SQLAlchemy

login_manager = LoginManager() #helps us handle login/outsessions

#Load config file
def create_app(config_name):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile('config.py')
	db.init_app(app)
	return app

	login_manager.init_app(app)
	login_manager.login_message = "You must be logged in to access thi page."
	login_manager.login_view ='signin'
	login_manager.session_protection = 'strong'

'''
	@app.route('/')
	def hello_world():
		return 'Hello, World!'
'''
from app import models

