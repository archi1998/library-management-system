# src/library.py
from src.book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, isbn):
        self.books = [b for b in self.books if b.isbn != isbn]

    def find_book(self, title):
        return [b for b in self.books if b.title.lower() == title.lower()]
