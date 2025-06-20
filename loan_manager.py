# fichier  loan_manager.py 
from datetime import datetime
from data_manager import save_books
from datetime import date, timedelta

def borrow_book(books, book_id, emprunteur):
    for book in books:
        if book["id"] == book_id and not book.get("emprunt", False):
            book["emprunt"] = True
            book["emprunteur"] = emprunteur
            book["date_emprunt"] = str(date.today())
            book["date_echeance"] = str(date.today() + timedelta(days=14))  # échéance 14 jours
            save_books(books)
            return True
    return False
def livres_en_retard(books):
    en_retard = []
    today = date.today()
    for book in books:
        if book.get("emprunt", False):
            date_echeance = date.fromisoformat(book.get("date_echeance", "2025-06-19"))
            if today > date_echeance:
                en_retard.append(book)
    return en_retard

def return_book(books, book_id):
    for book in books:
        if book["id"] == book_id and book.get("emprunt", False):
            book["emprunt"] = False
            book.pop("emprunteur", None)
            book.pop("date_emprunt", None)
            save_books(books)
            return True
    return False

def get_borrowed_books(books):
    return [book for book in books if book.get("emprunt", False)]

def get_available_books(books):
    return [book for book in books if not book.get("emprunt", False)]
