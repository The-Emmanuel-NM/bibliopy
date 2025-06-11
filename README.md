# 📚 BiblioPy – Projet de gestion de bibliothèque en ligne de commande

Projet réalisé par le **Groupe 56** dans le cadre du cours d'Algorithmique II.

---

## 🧠 Objectif

Créer un système simple de gestion de bibliothèque en Python, via une interface en ligne de commande, permettant de :
- Gérer une collection de livres
- Emprunter et retourner des livres
- Rechercher des livres par mot-clé
- Voir les emprunts des utilisateurs
- Générer un rapport d’emprunts (.txt)
- Sauvegarder automatiquement les données (JSON)

---

## 🏗️ Structure du projet

bibliopy-groupe/
│
├── gestion_donnees/
│ └── gestion_livres.py
│
├── emprunts/
│ ├── gestion_emprunts.py
│ ├── retour_emprunts.py
│ └── rapport_emprunts.py
│
├── recherche/
│ └── recherche_livres.py
│
├── emprunts/
│ └── emprunts.json ← données sauvegardées
│
├── main.py ← point d’entrée du programme
└── README.md



---

##  Lancer le programme

Dans PowerShell ou Terminal :

```bash
python main.py
```

## Menu principal
--- MENU ---
-1. Afficher les livres
-2. Ajouter un livre
-3. Emprunter un livre
-4. Voir les emprunts
-5. Retourner un livre
-6. Rechercher un livre
-7. Générer un rapport des emprunts (.txt)
-8. Quitter

##Sauvegarde automatique
-Les emprunts sont enregistrés dans le fichier emprunts/emprunts.json, ce qui permet de conserver les données même après fermeture du programme.


##Rapport
-Un fichier .txt est généré automatiquement via le menu pour afficher la liste des emprunts en cours.


# Membres du Groupe 56
[NGOY MELOA Emmanuel]

[NGOY BULUNGI Riben]

[NOTIA MUKOLA Anais]

[NGOY RAMAZANI Daniella]
