import eel
from random import randint
import main

# Set the web folder and the initial HTML file
eel.init("web")

@eel.expose
def greet_from_python():
    return "Hello from Python!"

@eel.expose    
def random_python():
    print("Random function running")
    return randint(1,100)

# from main import get_books_list

@eel.expose
# main.get_books_list()
def get_books():
    print(main.get_books_list())
    return main.get_books_list()


eel.start("index.html", size=(400, 300))
