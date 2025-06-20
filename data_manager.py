
##Module 1 : Gestion des Données & Persistance
##Ce module gère la lecture, l'écriture et la modification des livres dans un fichier CSV.

import csv

# Fichier CSV utilisé pour stocker les livres
DATA_FILE = "books.csv"

# Charger les livres depuis le fichier CSV
def load_books():
    books = []
    try:
        with open(DATA_FILE, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                books.append(row)
    except FileNotFoundError:
        pass  # Le fichier peut ne pas exister au début
    return books

# Sauvegarder les livres dans le fichier CSV
def save_books(books):
    with open(DATA_FILE, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["id", "titre", "auteur", "isbn", "annee", "statut"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for book in books:
            writer.writerow(book)

# Ajouter un livre au catalogue
def add_book(books, book):
    books.append(book)

# Supprimer un livre par ID
def delete_book(books, book_id):
    books[:] = [b for b in books if b["id"] != book_id]

# Modifier les informations d'un livre
def update_book(books, book_id, new_data):
    for book in books:
        if book["id"] == book_id:
            book.update(new_data)
            break
