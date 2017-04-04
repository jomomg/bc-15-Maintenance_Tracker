from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from config import app_config #third party imports
import os

basedir = os.path.abspath(os.path.dirname(__file__))

#initializa databse variable
db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'maintenancedb.sqlite')
    app.secret_key = '12345678'
    
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view ='auth.login'

    
    Bootstrap(app)

    from app import models

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)
    from .req import req as req_blueprint
    app.register_blueprint(req_blueprint)

    return app
