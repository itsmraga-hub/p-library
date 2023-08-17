from models.book import Book
from models import storage
import uuid


class BookManager:
  def __init__(self):
    self.book = Book()

  def create_book(self):
    book = Book()
    Book.save()

  def list_books(self):
    books = storage.all(Book).values()
    books = sorted(books, key=lambda book: book.id)
    return books