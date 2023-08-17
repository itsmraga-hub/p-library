from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import create_engine, Column, Integer, String
from models.base_model import BaseModel, Base
from hashlib import md5


class User(BaseModel, Base):
  __tablename__ = 'users'

  role = Column(String(128), default='member')
  name = Column(String(128), nullable=False)
  email = Column(String(128), nullable=False)
  password = Column(String(256), nullable=False)
  books = relationship("Book", backref='user', cascade="all, delete, delete-orphan")

  def __init__(self, *args, **kwargs):
    """initializes user"""
    super().__init__(*args, **kwargs)

  def __setattr__(self, name, value):
    """sets a password with md5 encryption"""
    if name == "password":
        value = md5(value.encode()).hexdigest()
    super().__setattr__(name, value)