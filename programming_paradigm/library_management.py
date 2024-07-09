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

# Example usage:
if __name__ == "__main__":
    my_library = Library()

    # Create some book instances
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")

    # Add books to the library
    my_library.add_book(book1)
    my_library.add_book(book2)

    # Check out a book
    my_library.check_out_book("The Great Gatsby")

    # List available books
    my_library.list_available_books()
