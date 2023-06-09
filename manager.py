'''
API REST
Personal use book management system.
Author -> 0xrauros
LICENSE -> Do what the fuck you want.

Remember:
> export FLASK_APP=manager.py
> flask run


'''
import os
from app import create_app, db
from flask_migrate import Migrate


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

print(app.config)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db)
