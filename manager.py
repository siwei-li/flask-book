from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from api_app import app, db
from models import Book, User


manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
