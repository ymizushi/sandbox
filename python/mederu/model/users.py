from mederu import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120))
    password = db.Column(db.String(80))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def add(self):
        db.create_all()
        db.session.add(self)

    def __repr__(self):
        return '<User %r, %r, %r>' % (self.username, self.email, self.password)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120))
    password = db.Column(db.String(80))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def add(self):
        db.create_all()
        db.session.add(self)

    def __repr__(self):
        return '<User %r, %r, %r>' % (self.username, self.email, self.password)
