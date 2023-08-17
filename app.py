from colorama import Fore
from manager.book_manager import BookManager

class App:
    def __init__(self, action):
        self._action = action.strip().lower()
        self.book_manager = BookManager()

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, action):
        self._action = action

    def display(self):
        print('[1] - List available books')
        print('[2] - Add books')
        print('[3] - Delete book')
        print('[4] - Update book')
        print('[5] - Sell book')
        print('[6] - Lend book')
        self._action = input(Fore.GREEN + '>> ' + Fore.WHITE)
        print(self._action)


    def manage(self):
        self.display()
        try:
            if self.action == '1':
                self.book_manager.list_books()
        except Exception as e:
            print(f'Failed - {e}')


    def run(self):
        try:
            while True:
                if self._action == 'q':
                    print('bye')
                    exit()
                if self._action == 'l':
                    print('Login')
                    self.manage()
                if self._action == 'c':
                    print('Sign up')
        except KeyboardInterrupt:
            print()
            print('bye')
            exit()
