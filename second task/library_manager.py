from library_interface import LibraryInterface
from book import Book

class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: str) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)
    
    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)
    
    def show_books(self) -> None:
        self.library.show_books()