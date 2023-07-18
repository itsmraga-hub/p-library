from models.user import User
from models.book import Book
from models.category import Category


class Main:
    def __init__(self):
        pass

    def menu():
        print('Welcome to P-Library')
        print('Choose an option below:')
        print('1: Add book Category')
        print('2: Add book')
        print('3: Add user')
        print('4: Exit')
        print()
        Main.take_input()

    def take_input():
        arg = input('Enter choice: ')
        print()

    def run(self):
        while True:
            Main.menu()


m = Main()
m.run()


import sqlalchemy
from sqlalchemy import create_engine


HBNB_MYSQL_USER = 'raga'
HBNB_MYSQL_PWD = 'root'
HBNB_MYSQL_HOST = '127.0.0.1'
HBNB_MYSQL_PORT = 5432
HBNB_MYSQL_DB = 'p_library'
engine = create_engine(f'postgresql://{HBNB_MYSQL_USER}:{HBNB_MYSQL_PWD}@{HBNB_MYSQL_HOST}:{HBNB_MYSQL_PORT}/{HBNB_MYSQL_DB}')

# Test the connection
# try:
#     with engine.connect() as connection:
#         print("Connection successful!")
# except Exception as e:
#     print(f"Connection error: {str(e)}")