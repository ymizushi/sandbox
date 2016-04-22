#!env python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
db = SQLAlchemy(app)
import model.users
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/mederu.db'

app.secret_key='hogehoge'
# 
import apps.frontend.views
app.register_blueprint(apps.frontend.views.frontend)

import apps.admin.views
app.register_blueprint(apps.admin.views.admin)


if __name__ == "__main__":
    app.run(debug=config.App)
