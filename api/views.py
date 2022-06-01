from flask import Blueprint, jsonify, request
from api import db
from api.BookShelfDB import BookDB
import pandas as pd
import json

main = Blueprint('main', __name__)

@main.route("/add_book", methods=['POST'])
def add_book():
    data = request.json
    title, author, tpages = data['title'], data["author"], data["pages"]
    db = BookDB()
    try:
        db.insert(author, title, tpages.strip())
        print("OK")
        return "200"
    except:
        return "500"

@main.route("/update_book", methods=['POST'])
def update_book():
    data = request.json
    id, field, new_value = data[0], data[1], data[2]
    db = BookDB()
    try:
        db.update(id, field, new_value)
        return "200"
    except:
        return "500"

@main.route("/delete_book", methods=['POST'])
def delete_book():
    data = request.json
    id = data
    db = BookDB()
    try:
        for i in id:
            db.delete(i)
        return "200"
    except:
        return "500"


@main.route("/get_all_books", methods=['GET'])
def get_all_books():
    db = BookDB()
    try:
        data_book = db.pull_all_data()
        return data_book
    except:
        return 500

@main.route("/get_all_books_em_espera", methods=['GET'])
def get_all_books_em_espera():
    db = BookDB()
    try:
        data_book = db.pull_filtered_data("LISTA DE ESPERA")
        return data_book
    except:
        return 500

@main.route("/get_all_books_ativos", methods=['GET'])
def get_all_books_ativos():
    db = BookDB()
    try:
        data_book = db.pull_filtered_data("ATIVO")
        return data_book
    except:
        return 500

@main.route("/get_all_books_conclusos", methods=['GET'])
def get_all_books_conclusos():
    db = BookDB()
    try:
        data_book = db.pull_filtered_data("CONCLUSO")
        return data_book
    except:
        return 500
    