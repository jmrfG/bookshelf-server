from api.models import Books
from api import db, create_app

if __name__=="__main__":
    db.create_all(app=create_app())