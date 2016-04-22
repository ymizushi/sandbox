#!env python3

from mederu import db
db.create_all()

from model.users import User
admin = User('admin', 'admin@example.com', 'piyopiy')
guest = User('guest', 'guest@example.com', 'hufgahuga')

db.session.add(admin)
db.session.add(guest)
db.session.commit()
