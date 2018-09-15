from app import create_app

# script import manger
from flask_script import Manager, Server


app = create_app('development')

# difineing a manager to app
manager = Manager(app)


manager.add_command('server', Server)

if __name__ == '__main__':
    manager.run()
