# import PySide6.QtCore

# # Prints PySide6 version
# print(PySide6.__version__)

# # Prints the Qt version used to compile PySide6
# print(PySide6.QtCore.__version__)


import sys
from PySide6.QtWidgets import QApplication, QLabel, QPushButton
from PySide6.QtCore import Slot


# Greetings
@Slot()
def say_hello():
    print("Button clicked, Hello!")

app = QApplication(sys.argv)
# Create a button
button = QPushButton("Click me")
# Connect the button to the function
button.clicked.connect(say_hello)
label = QLabel("Hello World!")
# This HTML approach will be valid too!
label2 = QLabel("<font color=red size=40>Hello World!</font>")
label.show()
label2.show()
# Show the button
button.show()
# Run the main Qt loop
# app.exec()
app.exec()