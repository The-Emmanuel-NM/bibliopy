def tri_bulle(livres, cle):
    """Trie les livres avec l'algorithme du tri à bulles, selon la clé choisie (titre, auteur, année)."""
    n = len(livres)
    for i in range(n):
        for j in range(0, n - i - 1):
            if str(livres[j][cle]).lower() > str(livres[j + 1][cle]).lower():
                livres[j], livres[j + 1] = livres[j + 1], livres[j]
    return livres

def tri_selection(livres, cle):
    """Trie les livres avec le tri par sélection, selon la clé choisie."""
    n = len(livres)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if str(livres[j][cle]).lower() < str(livres[min_index][cle]).lower():
                min_index = j
        livres[i], livres[min_index] = livres[min_index], livres[i]
    return livres
