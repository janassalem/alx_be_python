class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book from the library by title."""
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return False

    def return_book(self, title):
        """Return a book to the library by title."""
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return False

    def list_available_books(self):
        """List all available books in the library."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")


# Main script for testing (main.py)
if __name__ == "__main__":
    from library_management import Book, Library

    def main():
        # Setup a small library
        library = Library()
        library.add_book(Book("Brave New World", "Aldous Huxley"))
        library.add_book(Book("1984", "George Orwell"))

        # Initial list of available books
        print("Available books after setup:")
        library.list_available_books()

        # Simulate checking out a book
        library.check_out_book("1984")
        print("\nAvailable books after checking out '1984':")
        library.list_available_books()

        # Simulate returning a book
        library.return_book("1984")
        print("\nAvailable books after returning '1984':")
        library.list_available_books()

    main()
