from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    passwod = db.Column(db.String(80), unique=True)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = passwod

    def __repr__(self):
        return '<User %r, %r, %r>' % (self.username, self.email, self.password)
