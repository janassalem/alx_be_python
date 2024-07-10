class Book:
      def __init__(self, title, author,):
           self.title = title
           self.author = author
           
class Library:
       def __init__(self):
           self._books = []
           self.__is_checked_out = True
           
       def add_book(self,book):
             self._books.append(book)   
                  
       def list_available_books(self):
             for book in self._books:
                 return  book.title,book.author
       def check_out_book(self,title):
             for book in self._books:
                 if title == book.title:
                    return True   
             return False  
       def return_book(self):
             for book in self._books:
                 return  book.title,book.author
                       
library = Library()
library.add_book(Book("Brave New World", "Aldous Huxley"))
library.add_book(Book("1984", "George Orwell"))
print(library.list_available_books())
print(library.check_out_book("1984"))
