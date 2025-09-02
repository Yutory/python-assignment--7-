"""
Library Management System

Task:
- Create functions to manage a library using dictionaries and lists.
- Each book is stored in a dictionary with fields: { "id": int, "title": str, "author": str, "available": bool }
- Users can borrow and return books.
- Support *args for searching books by multiple fields (title, author).
- Support **kwargs for adding optional book details like "year", "genre".


// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Books as a Book class.
- Library as a Library class with borrow() and return() methods.
"""

library = []

def add_book(book):
    """Add a new book into the library with flexible details.
        return "Book {book_title} added successfully!"
    """

def search_books(search_param):
    """Search for books by multiple keywords (title, author).
    return books that match search description.
    """

def borrow_book(book_id):
    """Borrow a book if available (msg: You borrowed {book_title}).
        else-> msg: Book {book_title} not available
    """

library = []

def add_book(book_id, title, author, **kwargs):
    """Add a new book into the library with flexible details."""
    # Check if book already exists
    for book in library:
        if book["id"] == book_id:
            return f"Book with ID {book_id} already exists!"

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "available": True
    }
    # Add optional details (year, genre, etc.)
    book.update(kwargs)

    library.append(book)
    return f"Book '{title}' added successfully!"


def search_books(*keywords):
    """
    Search for books by multiple keywords (title, author).
    Returns a list of matching books.
    """
    results = []
    for book in library:
        text = f"{book['title']} {book['author']}".lower()
        if all(keyword.lower() in text for keyword in keywords):
            results.append(book)
    return results


def borrow_book(book_id):
    """Borrow a book if available."""
    for book in library:
        if book["id"] == book_id:
            if book["available"]:
                book["available"] = False
                return f"You borrowed '{book['title']}'."
            else:
                return f"Book '{book['title']}' is not available."
    return f"Book with ID {book_id} not found."


def return_book(book_id):
    """Return a borrowed book."""
    for book in library:
        if book["id"] == book_id:
            if not book["available"]:
                book["available"] = True
                return f"You returned '{book['title']}'."
            else:
                return f"Book '{book['title']}' was not borrowed."
    return f"Book with ID {book_id} not found."


# ---------------- Example Run ----------------
print(add_book(1, "The Great Gatsby", "F. Scott Fitzgerald", year=1925, genre="Novel"))
print(add_book(2, "1984", "George Orwell", year=1949, genre="Dystopian"))
print(add_book(3, "Python Programming", "John Doe"))

print("\nSearch results:", search_books("python"))
print("\n", borrow_book(2))
print("\n", borrow_book(2))   # try borrowing again
print("\n", return_book(2))
print("\nSearch results:", search_books("George", "1984"))

