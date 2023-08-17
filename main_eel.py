from models.user import User
from models.book import Book


# import main
import sqlalchemy
import traceback
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


HBNB_MYSQL_USER = 'raga'
HBNB_MYSQL_PWD = 'root'
HBNB_MYSQL_HOST = '127.0.0.1'
HBNB_MYSQL_PORT = 5432
HBNB_MYSQL_DB = 'p_library'
engine = create_engine(f'postgresql://{HBNB_MYSQL_USER}:{HBNB_MYSQL_PWD}@{HBNB_MYSQL_HOST}:{HBNB_MYSQL_PORT}/{HBNB_MYSQL_DB}')


# Base.metadata.create_all(engine)

# Test the connection
def get_books_list():
    try:
        # with engine:
        Session = sessionmaker(bind=engine)
        session = Session()
        # with session:
        books = session.query(Book).all()
        book_list = []
        for book in books:
            book_list.append(book.__dict__)
        # print(books)
        # print(books[0].__dict__)
        # print("Connection successful!")
        return book_list
    except Exception as e:
        print(f"Connection error: {str(e)}")
        # traceback.print_exc()