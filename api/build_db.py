from .models import Books
from . import db, create_app

if __name__=="main":
    db.create_all(app=create_app())