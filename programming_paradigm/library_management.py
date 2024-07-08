class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Checks if the book is available."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Adds a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Checks out a book from the library by title."""
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return False

    def return_book(self, title):
        """Returns a book to the library by title."""
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return False

    def list_available_books(self):
        """Lists all available books in the library."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")


# Below code should be in the main.py file, for clarity purposes it is shown here
if __name__ == "__main__":
    # Example usage
    library = Library()
    book1 = Book("Brave New World", "Aldous Huxley")
    book2 = Book("1984", "George Orwell")

    library.add_book(book1)
    library.add_book(book2)

    print("Available books after setup:")
    library.list_available_books()

    print("\nChecking out '1984':")
    library.check_out_book("1984")

    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    print("\nReturning '1984':")
    library.return_book("1984")

    print("\nAvailable books after returning '1984':")
    library.list_available_books()