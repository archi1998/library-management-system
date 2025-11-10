# tests/test_member.py
from src.book import Book
from src.member import Member

def test_member_borrow_return():
    member = Member("Alice")
    book = Book("1984", "Orwell", "123")
    assert member.borrow_book(book) == True
    assert book.available == False
    member.return_book(book)
    assert book.available == True
