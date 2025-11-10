# tests/test_library.py
from src.book import Book
from src.library import Library

def test_add_and_remove_book():
    lib = Library()
    b = Book("1984", "Orwell", "123")
    lib.add_book(b)
    assert lib.find_book("1984") == [b]
    lib.remove_book("123")
    assert lib.find_book("1984") == []
