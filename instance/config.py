import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'maintenancedb.sqlite')

SECRET_KEY = 'ABc#@tGQW'