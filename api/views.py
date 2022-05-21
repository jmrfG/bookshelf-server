from flask import Blueprint, jsonify, request
from api import db
from api.models import Books

main = Blueprint('main', __name__)

@main.route("/add_book", methods=['POST'])
def add_book():
    data = request.json
    new_book = Books(title=data['title'], author=data["author"])
    db.session.add(new_book)
    db.session.commit()
    return 'Book registered', 200

@main.route("/get_all_books", methods=['GET'])
def get_all_books():
    b = Books.query.all()
    books = []

    for i in b:
        books.append({'title':i.title, 'author':i.author})
    return jsonify({'books': books})