from app import App
from colorama import Fore
from models.engine import storage


def display():
  print()
  print(Fore.GREEN + 'Welcome to P-Library' + Fore.WHITE)
  print()
  print('Enter a command below to get started')
  print('[C] - Create Account')
  print('[L] - Log In')
  print('')
  print('Q - Quit')
  print('')

def main():
  display()
  action = input(Fore.GREEN + '>> ' + Fore.WHITE)
  app = App(action)
  app.run()


if __name__ == '__main__':
  main()