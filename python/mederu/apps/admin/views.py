from flask import Blueprint, render_template
from jinja2 import TemplateNotFound
admin = Blueprint('admin', __name__, url_prefix='/admin', template_folder='templates', static_folder='static')

import model.users

@admin.route('/')
def index():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)

@admin.route('/admin_users')
def admin_users():
    try:
        return render_template('admin_users.html')
    except TemplateNotFound:
        abort(404)

def create_user():
    user = model.users.User('hoge', 'admin@example.com', 'hogehoge')
    user.add()

@admin.route('/users')
def users():
    users = model.users.User.query.all()
    return render_template('users.html', users=users)

@admin.route('/characters')
def characters():
    try:
        return render_template('characters.html')
    except TemplateNotFound:
        abort(404)

@admin.route('/tweets')
def tweets():
    try:
        return render_template('tweets.html')
    except TemplateNotFound:
        abort(404)

@admin.route('/works')
def works():
    try:
        return render_template('works.html')
    except TemplateNotFound:
        abort(404)

@admin.route('/tags')
def tags():
    try:
        return render_template('tags.html')
    except TemplateNotFound:
        abort(404)
