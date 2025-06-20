
#Module 4 : Gestion des Emprunts
#Gère l'emprunt et le retour des livres.

# Marquer un livre comme emprunté
def borrow_book(books, book_id, emprunteur):
    for book in books:
        if book["id"] == book_id:
            book["statut"] = f"emprunté par {emprunteur}"
            break

# Marquer un livre comme retourné
def return_book(books, book_id):
    for book in books:
        if book["id"] == book_id:
            book["statut"] = "disponible"
            break

# Lister tous les livres empruntés
def list_borrowed_books(books):
    return [book for book in books if book["statut"].startswith("emprunté")]

# Lister les livres disponibles
def list_available_books(books):
    return [book for book in books if book["statut"] == "disponible"]
