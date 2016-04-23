from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from jinja2 import TemplateNotFound
import model.users

admin = Blueprint('admin', __name__, url_prefix='/admin', template_folder='templates', static_folder='static')


def is_login(session):
    return session.get('logged_in')

@admin.route('/', methods=['GET'])
def index():
    if is_login(session):
        return render_template('admin/index.html')
    else:
        return redirect(url_for('admin.login'))

def get_user(email):
    return model.users.User.query.filter_by(email=email).first()


@admin.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('admin/login.html')
    else:
        email = request.form['mail']
        user = get_user(email)
        if user and user.password == request.form.get('password'):
             session['logged_in'] = True
             flash('You were logged in')
             return redirect(url_for('admin.index'))
        return redirect(url_for('admin.index'))

@admin.route('/logout', methods=['GET'])
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('admin.login'))

@admin.route('/admin_users')
def admin_users():
    if not is_login(session):
        return redirect(url_for('admin.login'))
    try:
        return render_template('admin/admin_users.html')
    except TemplateNotFound:
        abort(404)

def create_user():
    user = model.users.User('hoge', 'admin@example.com', 'hogehoge')
    user.add()

@admin.route('/users')
def users():
    if not is_login(session):
        return redirect(url_for('admin.login'))
    users = model.users.User.query.all()
    return render_template('admin/users.html', users=users)

@admin.route('/characters')
def characters():
    if not is_login(session):
        return redirect(url_for('admin.login'))
    try:
        return render_template('admin/characters.html')
    except TemplateNotFound:
        abort(404)

@admin.route('/tweets')
def tweets():
    if not is_login(session):
        return redirect(url_for('admin.login'))
    try:
        return render_template('admin/tweets.html')
    except TemplateNotFound:
        abort(404)

@admin.route('/works')
def works():
    if not is_login(session):
        return redirect(url_for('admin.login'))
    try:
        return render_template('admin/works.html')
    except TemplateNotFound:
        abort(404)

@admin.route('/tags')
def tags():
    if not is_login(session):
        return redirect(url_for('admin.login'))
    try:
        return render_template('admin/tags.html')
    except TemplateNotFound:
        abort(404)
