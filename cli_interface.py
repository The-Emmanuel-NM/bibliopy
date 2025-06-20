
#Module 5 : Interface Utilisateur et Rapports
#Gère le menu en ligne de commande pour l'interaction avec l'utilisateur.

import data_manager
import loan_manager
import sort_engine
import search_engine

def afficher_menu():
    print("\n=== BiblioPy ===")
    print("1. Afficher tous les livres")
    print("2. Ajouter un livre")
    print("3. Supprimer un livre")
    print("4. Rechercher un livre")
    print("5. Trier les livres")
    print("6. Emprunter un livre")
    print("7. Retourner un livre")
    print("8. Afficher livres empruntés")
    print("9. Quitter")

def lancer_interface():
    livres = data_manager.load_books()
    while True:
        afficher_menu()
        choix = input("Choix : ")
        if choix == "1":
            for livre in livres:
                print(livre)
        elif choix == "2":
            livre = {
                "id": input("ID: "),
                "titre": input("Titre: "),
                "auteur": input("Auteur: "),
                "isbn": input("ISBN: "),
                "annee": input("Année: "),
                "statut": "disponible"
            }
            data_manager.add_book(livres, livre)
            data_manager.save_books(livres)
        elif choix == "3":
            book_id = input("ID à supprimer: ")
            data_manager.delete_book(livres, book_id)
            data_manager.save_books(livres)
        elif choix == "4":
            critere = input("Critère (titre/auteur/isbn): ")
            valeur = input("Valeur à rechercher: ")
            resultats = search_engine.sequential_search(livres, critere, valeur)
            for r in resultats:
                print(r)
        elif choix == "5":
            cle = input("Trier par (titre/auteur/annee): ")
            livres = sort_engine.bubble_sort(livres, cle)
        elif choix == "6":
            book_id = input("ID du livre: ")
            emprunteur = input("Nom de l'emprunteur: ")
            loan_manager.borrow_book(livres, book_id, emprunteur)
            data_manager.save_books(livres)
        elif choix == "7":
            book_id = input("ID du livre: ")
            loan_manager.return_book(livres, book_id)
            data_manager.save_books(livres)
        elif choix == "8":
            empruntes = loan_manager.list_borrowed_books(livres)
            for livre in empruntes:
                print(livre)
        elif choix == "9":
            data_manager.save_books(livres)
            break
        else:
            print("Choix invalide.")
