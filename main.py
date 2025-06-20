# === main.py ===
import data_manager
import cli_interface
import loan_manager
import search_engine
import sort_engine

def main():
    books = data_manager.load_books()

    while True:
        cli_interface.afficher_menu()  # <-- Ajoute cette ligne
        choix = cli_interface.demander_entree(" Votre choix : ", int)

        if choix == 1:
            titre = input("Titre : ")
            auteur = input("Auteur : ")
            isbn = input("ISBN : ")
            annee = cli_interface.demander_entree("Année : ", int)
            new_id = data_manager.generate_new_id(books)
            nouveau_livre = {
                "id": new_id,
                "titre": titre,
                "auteur": auteur,
                "isbn": isbn,
                "annee": annee,
                "emprunt": False
            }
            data_manager.add_book(books, nouveau_livre)
            print("Livre ajouté avec succès.")

        elif choix == 2:
            book_id = cli_interface.demander_entree("ID du livre à supprimer : ", int)
            data_manager.delete_book(books, book_id)
            print("Livre supprimé.")

        elif choix == 3:
            book_id = cli_interface.demander_entree("ID du livre à modifier : ", int)
            for book in books:
                if book["id"] == book_id:
                    titre = input(f"Titre [{book['titre']}] : ") or book["titre"]
                    auteur = input(f"Auteur [{book['auteur']}] : ") or book["auteur"]
                    isbn = input(f"ISBN [{book['isbn']}] : ") or book["isbn"]
                    annee = input(f"Année [{book['annee']}] : ") or book["annee"]
                    updated = {
                        "titre": titre,
                        "auteur": auteur,
                        "isbn": isbn,
                        "annee": int(annee)
                    }
                    data_manager.update_book(books, book_id, updated)
                    print("Livre modifié.")
                    break
            else:
                print("Livre non trouvé.")

        elif choix == 4:
            print("Rechercher par : 1. Titre  2. Auteur  3. ISBN")
            champ = cli_interface.demander_entree("Votre choix : ", int)
            cles = {1: "titre", 2: "auteur", 3: "isbn"}
            if champ in cles:
                mot = input("Mot-clé : ")
                resultat = search_engine.linear_search(books, mot, cles[champ])
                cli_interface.afficher_livres(resultat)
            else:
                print("Choix invalide.")

        elif choix == 5:
            print("Trier par : 1. Titre  2. Auteur  3. Année")
            champ = cli_interface.demander_entree("Votre choix : ", int)
            cles = {1: "titre", 2: "auteur", 3: "annee"}
            if champ in cles:
                sort_engine.insertion_sort(books, cles[champ])
                cli_interface.afficher_livres(books)
            else:
                print("Choix invalide.")

        elif choix == 6:
            book_id = cli_interface.demander_entree("ID du livre à emprunter : ", int)
            nom = input("Nom de l’emprunteur : ")
            if loan_manager.borrow_book(books, book_id, nom):
                print("Livre emprunté.")
            else:
                print("Impossible d’emprunter ce livre.")

        elif choix == 7:
            book_id = cli_interface.demander_entree("ID du livre à retourner : ", int)
            if loan_manager.return_book(books, book_id):
                print("Livre retourné.")
            else:
                print("Ce livre n'était pas emprunté.")

        elif choix == 8:
            afficher_rapport(books)

        elif choix == 9:
            cli_interface.afficher_livres_en_retard(books)

        elif choix == 10:
            print("À bientôt !")
            break
        
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()
