import json
import os
# gestion_emprunts.py
fichier_json = "emprunts/emprunts.json"
emprunts = {}  # Clé : nom de l'utilisateur, Valeur : liste de livres empruntés
def charger_emprunts():
    global emprunts
    if os.path.exists(fichier_json):
        with open(fichier_json, "r") as f:
            emprunts = json.load(f)
    else:
        emprunts = {}
def sauvegarder_emprunts():
    with open(fichier_json, "w", encoding="utf-8") as f:
        json.dump(emprunts, f, indent=4, ensure_ascii=False)

def emprunter_livre(utilisateur, titre):
    if utilisateur in emprunts:
        emprunts[utilisateur].append(titre)
    else:
        emprunts[utilisateur] = [titre]
    print(f"\n📖 {utilisateur} a emprunté le livre : {titre}")
    sauvegarder_emprunts()

def afficher_emprunts():
    print("\n📋 Liste des emprunts :")
    if not emprunts:
        print("Aucun emprunt enregistré.")
    else:
        for utilisateur, livres in emprunts.items():
            print(f"- {utilisateur} a emprunté : {', '.join(livres)}")
            
