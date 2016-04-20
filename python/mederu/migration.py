#!env python3
from server import db
db.create_all()

from server import User
admin = User('admin', 'admin@example.com')
guest = User('guest', 'guest@example.com')

db.session.add(admin)
db.session.add(guest)
db.session.commit()

users = User.query.all()
admin = User.query.filter_by(username='admin').first()
