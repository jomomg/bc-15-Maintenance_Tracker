from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#from config import app_config

#initialize the app
app = Flask(__name__, instance_relative_config=True)

#Load the views
from app import views

#load config file
app.config.from_object('config')

#db = SQLAlchemy
#Load config file
'''def create_app(config_name):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile('config.py')
	db.init_app(app)

	@app.route('/')
	def hello_world():
		return 'Hello, World!'

	return app
'''