from library_interface import LibraryInterface
from book import Book

class Library(LibraryInterface):
    def __init__(self):
        self.books = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, title: str) -> None:
        self.books = [book for book in self.books if book.title != title]

    def show_books(self) -> None:
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, Year: {book.year}")