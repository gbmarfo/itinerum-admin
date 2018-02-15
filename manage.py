#!/usr/bin/env python
# Kyle Fitzsimmons, 2017-2018
#
# Entry point to run API, migrations and helper scripts
from flask_migrate import MigrateCommand
from flask_script import Manager, Server
import logging

from admin.server import create_app


logging.getLogger('itinerum.admin').setLevel(logging.WARNING)

app = create_app()
server = Server(port=app.config['APP_PORT'])
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', server)


@manager.command
def reset():
    logging.warn('Dropping and creating database tables...')
    db = app.extensions['sqlalchemy'].db
    db.drop_all()
    db.create_all()


if __name__ == '__main__':
    manager.run()

