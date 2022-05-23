from flask import Blueprint, jsonify, request
from api import db
from api.BookShelfDB import BookDB
import pandas as pd
import json

main = Blueprint('main', __name__)

@main.route("/add_book", methods=['POST'])
def add_book():
    data = request.json
    new_book = data['title'], data["author"]
    
    return 'Book registered', 200

@main.route("/get_all_books", methods=['GET'])
def get_all_books():
    db = BookDB()
    try:
        data_book = db.pull_all_data()
        return data_book
    except:
        return 500
    