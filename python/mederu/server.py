#!env python3

from flask import Flask, Blueprint
from flask import session, redirect, url_for, escape, request
from flask_sqlalchemy import SQLAlchemy
import config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/mederu.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

def login_filter(f):
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for(''))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''
    return f

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

app.secret_key='hogehoge'

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


from app.admin.views import admin
app.register_blueprint(admin)

if __name__ == "__main__":
    app.run(debug=config.App)
