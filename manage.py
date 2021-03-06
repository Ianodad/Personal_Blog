
from app import create_app, db


# script import manger
from flask_script import Manager, Server

# user imports models
from app.models import User, Blog, Comment, Subscribe

# flash extension for migrating
from flask_migrate import Migrate, MigrateCommand

# app = create_app('development')
app = create_app('production')


# difineing a manager to app
manager = Manager(app)

# access to the shell


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Blog=Blog, Comment=Comment, Subscribe=Subscribe)


# intiate migrate class
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


# adding manager to serve
manager.add_command('server', Server)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
