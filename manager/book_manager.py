from models.book import Book
from models.engine import storage
import uuid


class BookManager:
  def __init__(self):
    self.book = Book()

  def create_book(self):
    book = Book()
    Book.save()

  def list_books(self):
    print(storage.__dict__)
    books = storage.all(Book).values()
    books = sorted(books, key=lambda book: book.id)
    return books