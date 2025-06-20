# cli_interface.py
from rich.console import Console
from rich.table import Table
from loan_manager import livres_en_retard

# Affichage du tableau des livres
def afficher_livres(books):
    console = Console()
    if not books:
        console.print("[bold red]Aucun livre trouvé.[/bold red]")
        return
    table = Table(title="Catalogue de Livres")
    table.add_column("ID", justify="center")
    table.add_column("Titre", style="bold")
    table.add_column("Auteur")
    table.add_column("Année")
    table.add_column("ISBN")
    table.add_column("Statut")
    for book in books:
        statut = "📚 Emprunté" if book.get("emprunt") else "✅ Disponible"
        table.add_row(str(book["id"]), book["titre"], book["auteur"], str(book["annee"]), book["isbn"], statut)
    console.print(table)

# Afficher les livres en retard
def afficher_livres_en_retard(books):
    en_retard = livres_en_retard(books)
    console = Console()

    if not en_retard:
        console.print("\n[bold green]Aucun livre en retard.[/bold green]\n")
        return

    table = Table(title="📕 Livres en Retard")
    table.add_column("ID", justify="center")
    table.add_column("Titre")
    table.add_column("Auteur")
    table.add_column("Emprunteur")
    table.add_column("Date d'échéance")

    for book in en_retard:
        table.add_row(
            str(book["id"]),
            book["titre"],
            book["auteur"],
            book.get("emprunteur", "N/A"),
            book.get("date_echeance", "")
        )

    console.print(table)
def afficher_menu():
    """Affiche le menu principal"""
    print("===== BiblioPy =====")
    print("1. Ajouter un livre")
    print("2. Supprimer un livre")
    print("3. Modifier un livre")
    print("4. Rechercher un livre")
    print("5. Afficher les livres triés")
    print("6. Emprunter un livre")
    print("7. Retourner un livre")
    print("8. Rapport")
    print("9. Date d'emprunt")
    print("10. Quitter")

def demander_entree(msg, type_=str):
    """Demande une entrée utilisateur avec validation"""
    try:
        return type_(input(msg))
    except ValueError:
        print("Entrée invalide.")
        return demander_entree(msg, type_)
