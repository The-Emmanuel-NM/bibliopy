# === search_engine.py ===
def linear_search(books, keyword, key):
    return [book for book in books if keyword.lower() in str(book[key]).lower()]

def binary_search(books, keyword, key):
    left, right = 0, len(books) - 1
    results = []
    while left <= right:
        mid = (left + right) // 2
        mid_value = str(books[mid][key]).lower()
        if keyword.lower() == mid_value:
            results.append(books[mid])
            break
        elif keyword.lower() < mid_value:
            right = mid - 1
        else:
            left = mid + 1
    return results
