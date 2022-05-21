from . import db

class Books(db.Model):
    idx = db.Column(db.Integer, primary_key=True)
    title, author = db.Column(db.String(50)), db.Column(db.String(50))
    