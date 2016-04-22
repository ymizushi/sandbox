from mederu import db

class Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(256))
    image_url = db.Column(db.String(256))

    def __init__(self, description, image_url):
        self.description = description
        self.image_url = image_url

    def add(self):
        db.session.add(self)

    def __repr__(self):
        return '<User %r, %r, %r>' % (self.username, self.email, self.password)

