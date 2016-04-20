#!env python3

from flask import Flask, Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy
from jinja2 import TemplateNotFound
import config

admin = Blueprint('admin', __name__, url_prefix='/admin', template_folder='templates')
@admin.route('/')
def index():
    try:
        return render_template('admin/index.html')
    except TemplateNotFound:
        abort(404)
