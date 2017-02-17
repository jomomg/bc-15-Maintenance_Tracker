import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db

config_name = os.getenv('FLASK_CONFIG') or 'development'
app = create_app(config_name)

if __name__ == '__main__':
    migrate = Migrate(app, db)

    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    manager.run()