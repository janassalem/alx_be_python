# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

    def is_available(self):
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return f"Checked out '{title}'"
        return f"'{title}' is not available"

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return f"Returned '{title}'"
        return f"'{title}' is not checked out"

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books available")
        else:
            for book in available_books:
                print(book)
