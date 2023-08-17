from models.user import User
from models import storage
import uuid


class UserManager:
  def __init__(self):
    self.book = User()

  def create_user(self):
    name = input('What is the user\'s name? ')
    # role = input('What is the user\'s name? ')
    email = input('What is the user\'s email? ')
    password = input('What is the user\'s password? ')
    user = User(
      name=name,
      email=email,
      password=password
    )
    user.save()

  def list_users(self):
    users = storage.all(User).values()
    # users = sorted(users, key=lambda user: user.id)
    print(users)
    return users