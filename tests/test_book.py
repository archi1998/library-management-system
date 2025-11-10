# tests/test_book.py
from src.book import Book

def test_borrow_and_return():
    b = Book("1984", "Orwell", "123")
    assert b.borrow() == True
    assert b.available == False
    assert b.borrow() == False
    b.return_book()
    assert b.available == True
