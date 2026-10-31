raw_books = [
    {
        "book_code": "B301", 
        "category": "science",
        "price": 185000, 
        "status": "available"
    },
    {
        "book_code": "b101 ", 
        "category": "novel",
        "price": 95000, 
        "status": "available"
    },
    {
        "book_code": "B202", 
        "category": "history",
        "price": 240000, 
        "status": "borrowed"
    },
    {
        "book_code": "B102", 
        "category": "novel",
        "price": 120000, 
        "status": "lost"
    },
    {
        "book_code": "B302", 
        "category": "science",
        "price": 210000, 
        "status": "available"
    }
]

def clean_and_validate_books(book_list):
    clean_book = []

    for book in book_list:
        book["book_code"] = book["book_code"].strip().upper()

        if book["book_code"].startswith("B") and book["book_code"][1:].isdigit():
            clean_book.append(book)

    return clean_book

# print(clean_and_validate_books(raw_books))

def search_books(book_list, status, price):
    find_book = []

    for book in book_list:
        if status:
            if book["status"] == status and book["price"] <= price:
                find_book.append(book)
        else:
            if book["price"] <= price:
                find_book.append(book)

    return find_book

# print(search_books(raw_books, "available", 120000))

def sort_books_by_price(book_list):
    n = len(book_list)

    for i in range(n):
        for j in range(n-i-1):
            if book_list[j]["price"] < book_list[j+1]["price"]:
                book_list[j], book_list[j+1] = book_list[j+1], book_list[j]

    return book_list

sort_book = sort_books_by_price(raw_books)
for book in sort_book:
    print(book)