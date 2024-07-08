class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Check out the book."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        else:
            return False

    def return_book(self):
        """Return the book."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        else:
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
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books available.")


# Main script for testing the library management system
if __name__ == "__main__":
    def main():
        library = Library()

        # Adding books to the library
        library.add_book(Book("Brave New World", "Aldous Huxley"))
        library.add_book(Book("1984", "George Orwell"))

        # Display available books
        print("Available books after setup:")
        library.list_available_books()

        # Check out a book
        print("\nChecking out '1984'...")
        if library.check_out_book("1984"):
            print("'1984' checked out successfully.")
        else:
            print("Failed to check out '1984'.")

        # Display available books after checking out
        print("\nAvailable books after checking out '1984':")
        library.list_available_books()

        # Return a book
        print("\nReturning '1984'...")
        if library.return_book("1984"):
            print("'1984' returned successfully.")
        else:
            print("Failed to return '1984'.")

        # Display available books after returning
        print("\nAvailable books after returning '1984':")
        library.list_available_books()

    main()
