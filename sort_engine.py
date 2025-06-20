# === sort_engine.py ===
def insertion_sort(books, key):
    for i in range(1, len(books)):
        current = books[i]
        j = i - 1
        while j >= 0 and str(books[j][key]) > str(current[key]):
            books[j + 1] = books[j]
            j -= 1
        books[j + 1] = current
