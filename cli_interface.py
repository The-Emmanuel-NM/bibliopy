from data_manager import DataManager
from search_engine import SearchEngine
from sort_engine import SortEngine
from loan_manager import LoanManager
from models import Book
import sys

class CLIInterface:
    def __init__(self):
        self.dm = DataManager()
        self.searcher = SearchEngine(self.dm.list_books)
        self.sorter = SortEngine(self.dm.list_books)
        self.loaner = LoanManager(self.dm)

    def _print_books(self, books):
        if not books:
            print("— Aucun livre trouvé —")
        for b in books:
            status = "Emprunté" if b.is_loaned else "Disponible"
            print(f"[{b.id}] {b.title} | {b.author} | {b.year} | {status}")

    def menu(self):
        while True:
            print("\n=== BiblioPy ===")
            print("1. Ajouter un livre")
            print("2. Supprimer un livre")
            print("3. Modifier un livre")
            print("4. Lister les livres")
            print("5. Rechercher un livre")
            print("6. Trier les livres")
            print("7. Emprunter un livre")
            print("8. Retourner un livre")
            print("9. Rapport")
            print("0. Quitter")
            choice = input("Choix: ").strip()
            try:
                {
                    "1": self._add,
                    "2": self._remove,
                    "3": self._update,
                    "4": self._list_all,
                    "5": self._search,
                    "6": self._sort,
                    "7": self._loan,
                    "8": self._return,
                    "9": self._report,
                    "0": sys.exit
                }[choice]()
            except KeyError:
                print("Option invalide.")
            except Exception as e:
                print(f"Erreur: {e}")

    def _add(self):
        nid = int(input("ID: "))
        title = input("Titre: ")
        author = input("Auteur: ")
        isbn = input("ISBN: ")
        year = int(input("Année de publication: "))
        book = Book(nid, title, author, isbn, year)
        self.dm.add_book(book)
        print("Livre ajouté.")

    def _remove(self):
        bid = int(input("ID du livre à supprimer: "))
        self.dm.remove_book(bid)
        print("Livre supprimé.")

    def _update(self):
        bid = int(input("ID du livre à modifier: "))
        book = self.dm.get_by_id(bid)
        print("Laissez vide pour ne pas changer.")
        title = input(f"Titre [{book.title}]: ") or book.title
        author = input(f"Auteur [{book.author}]: ") or book.author
        isbn = input(f"ISBN [{book.isbn}]: ") or book.isbn
        year = input(f"Année [{book.year}]: ")
        year = int(year) if year else book.year
        book.title, book.author, book.isbn, book.year = title, author, isbn, year
        self.dm.update_book(book)
        print("Livre modifié.")

    def _list_all(self):
        self._print_books(self.dm.list_books())

    def _search(self):
        crit = input("Par (titre/auteur/isbn) ? ").lower()
        term = input("Terme de recherche: ")
        use_bin = input("Utiliser recherche dichotomique si disponible ? (o/n): ").lower() == 'o'
        if crit == "titre":
            res = self.searcher.search_by_title(term, use_bin)
        elif crit == "auteur":
            res = self.searcher.search_by_author(term, use_bin)
        else:
            res = self.searcher.search_by_isbn(term)
        self._print_books(res)

    def _sort(self):
        crit = input("Trier par (titre/auteur/année) ? ").lower()
        method = input("Méthode (merge/bubble) ? ").lower()
        if crit == "titre":
            res = self.sorter.sort_by_title(method)
        elif crit == "auteur":
            res = self.sorter.sort_by_author(method)
        else:
            res = self.sorter.sort_by_year(method)
        self._print_books(res)

    def _loan(self):
        bid = int(input("ID du livre à emprunter: "))
        borrower = input("Nom de l’emprunteur: ")
        self.loaner.loan_book(bid, borrower)
        print("Emprunt enregistré.")

    def _return(self):
        bid = int(input("ID du livre à retourner: "))
        self.loaner.return_book(bid)
        print("Retour enregistré.")

    def _report(self):
        all_books = self.dm.list_books()
        loaned = len([b for b in all_books if b.is_loaned])
        total = len(all_books)
        print(f"Total livres   : {total}")
        print(f"Livres empruntés: {loaned}")
        print("Liste empruntés:")
        self._print_books(self.loaner.list_loaned())
