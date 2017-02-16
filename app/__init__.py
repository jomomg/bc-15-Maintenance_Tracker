from flask import Flask
#from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from config import app_config
from flask_login import LoginManager
from flask_migrate import Migrate

app = Flask(__name__)
app.secret_key = '12345678'

#initializa databse variable
db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_name):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile('config.py')
	db.init_app(app)

	login_manager.init_app(app)
	login_manager.login_message = "You must be logged in to access this page."
	login_manager.login_view ='auth.login'

	migrate = Migrate(app, db)

	from app import models

	return app



# login_manager = LoginManager() #helps us handle login/outsessions

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///maintenancedb'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# db.init_app(app)
# app.app_context().push()
# db.create_all()


# 
# login_manager.session_protection = 'strong'

#from app import views
