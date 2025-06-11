from gestion_donnees.gestion_livres import afficher_livre, ajouter_livre
from emprunts.gestion_emprunts import emprunter_livre, afficher_emprunts
from emprunts.retour_emprunts import retourner_livre
from emprunts.gestion_emprunts import charger_emprunts
from emprunts.rapport_emprunts import generer_rapport_txt
from recherche.recherche_livres import rechercher_livre

# gestion_donnees/gestion_livres.py
# main.py   
def main():
    charger_emprunts()
    while True:
        print("\n--- MENU ---")
        print("1. Afficher le livre")
        print("2. Ajouter un livre")
        print("3. Emprunter un livre")
        print("4. Voir les emprunts")
        print("5. Retourner un livre")
        print("6. Rechercher un livre")
        print("7. générer un rapport des emprunts")
        print("8. Quitter")

        choix = input("Choisis une option : ")

        if choix == "1":
            afficher_livres()
        elif choix == "2":
            titre = input("Titre du livre à ajouter : ")
            ajouter_livre(titre)
        elif choix == "3":
            utilisateur = input("Nom de l'utilisateur : ")
            titre = input("Titre du livre à emprunter : ")
            emprunter_livre(utilisateur, titre)
        elif choix == "4":
            afficher_emprunts()
        elif choix == "5":
            utilisateur = input("Nom de l'utilisateur : ")
            titre = input("Titre du livre à retourner : ")
            retourner_livre(utilisateur, titre)
        elif choix == "6":
            mot_cle = input("Entrez un mot clé pour la recherche : ")
            rechercher_livre(mot_cle)
        elif choix == "7":
            generer_rapport_txt()
        elif choix == "8":
            print("👋 Merci d'avoir utilisé le système de gestion de livres !")
            break
        else:
            print("❌ Option invalide. Réessaie.")

if __name__ == "__main__":
    main()
