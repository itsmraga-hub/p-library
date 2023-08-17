from colorama import Fore
from manager.book_manager import BookManager
from manager.user_manager import UserManager
from models.engine import storage

class App:
    def __init__(self, action):
        self._action = action.strip().lower()
        self.book_manager = BookManager()
        self.user_manager = UserManager()

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, action):
        self._action = action

    def display_users(self):
        print('[1] - list users')
        print('[2] - Create User')

    def display_books(self):
        print('[1] - List available books')
        print('[2] - Add books')
        print('[3] - Delete book')
        print('[4] - Update book')
        print('[5] - Sell book')
        print('[6] - Lend book')

    def display(self):
        self.display_users()
        self._action = int(input(Fore.GREEN + '>> ' + Fore.WHITE))


    def manage(self):
        self.display()
        # self.book_manager.list_books()
        try:
            if self.action == 1:
                # self.book_manager.list_books()
                self.user_manager.list_users()
            elif self.action == 2:
                self.user_manager.create_user()

            self.display()

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
