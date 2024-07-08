class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return False

    def list_available_books(self):
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")


if __name__ == "__main__":
    from library_management import Book, Library

    def main():
        library = Library()
        library.add_book(Book("Brave New World", "Aldous Huxley"))
        library.add_book(Book("1984", "George Orwell"))

        print("Available books after setup:")
        library.list_available_books()

        library.check_out_book("1984")
        print("\nAvailable books after checking out '1984':")
        library.list_available_books()

        library.return_book("1984")
        print("\nAvailable books after returning '1984':")
        library.list_available_books()

    main()
