#!env python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/mederu.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key='hogehoge'

@app.route('/')
def index():
    return "top"

db = SQLAlchemy(app)
import model.users
import model.admin_users
import model.characters
# 
import apps.admin.views
app.register_blueprint(apps.admin.views.admin)

import apps.frontend.views
app.register_blueprint(apps.frontend.views.frontend)



if __name__ == "__main__":
    app.run(debug=config.App)
