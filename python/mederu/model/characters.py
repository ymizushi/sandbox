from mederu import db

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    image_url = db.Column(db.String(80))

    def __init__(self, name, image_url):
        self.name = name
        self.image_url = image_url

    def add(self):
        db.session.add(self)

    def __repr__(self):
        return '<User %r, %r, %r>' % (self.username, self.email, self.password)

