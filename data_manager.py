# === data_manager.py ===
#Gestion des Données & Persistance
#Ce module gère la lecture, l'écriture et la modification des livres dans un fichier Json.

import json
import os

FILE_PATH = "books.json"

def initialize_file(file_path=FILE_PATH):
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump([], f)

def load_books(file_path=FILE_PATH):
    initialize_file(file_path)
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

#foncton pour enregistrer un livre
def save_books(books, file_path=FILE_PATH):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(books, f, indent=4, ensure_ascii=False)

#foncton pour ajouter un livre 
def add_book(books, new_book):
    books.append(new_book)
    save_books(books)

#foncton pour supprimer un livre
def delete_book(books, book_id):
    books[:] = [book for book in books if book["id"] != book_id]
    save_books(books)

#foncton pour mettre à jour un livre
def update_book(books, book_id, updated_info):
    for book in books:
        if book["id"] == book_id:
            book.update(updated_info)
            save_books(books)
            break

def generate_new_id(books):
    if not books:
        return 1
    return max(book["id"] for book in books) + 1
