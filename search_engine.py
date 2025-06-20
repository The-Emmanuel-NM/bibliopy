
#Module 2 : Algorithmes de Recherche
#Contient les fonctions de recherche séquentielle et dichotomique.

# Recherche séquentielle
def sequential_search(books, key, value):
    return [book for book in books if book[key].lower() == value.lower()]

# Recherche dichotomique (nécessite un tri préalable)
def binary_search(books, key, value):
    left, right = 0, len(books) - 1
    result = []
    while left <= right:
        mid = (left + right) // 2
        if books[mid][key].lower() == value.lower():
            result.append(books[mid])
            break
        elif books[mid][key].lower() < value.lower():
            left = mid + 1
        else:
            right = mid - 1 
    return result
