# -*- coding: utf-8 -*-

import os
import sys

from flask import Flask, render_template

from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

def install_secret_key(app, filename='secret_key'):
    filename = os.path.join(app.instance_path, filename)

    try:
        app.config['SECRET_KEY'] = open(filename, 'rb').read()
    except IOError:
        print('Error: No secret key. Create it with:')
        full_path = os.path.dirname(filename)
        if not os.path.isdir(full_path):
            print('mkdir -p {filename}'.format(filename=full_path))
        print('head -c 24 /dev/urandom > {filename}'.format(filename=filename))
        sys.exit(1)


if not app.config['DEBUG']:
    install_secret_key(app)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.route('/')
def index():
    return "/", 200

from app.admin.views import mod as admin
app.register_blueprint(admin)
from app.admin.users.views import mod as admin_users
app.register_blueprint(admin_users)

