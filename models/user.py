from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import create_engine, Column, Integer, String
from models.base_model import BaseModel, Base
from hashlib import md5


class User(BaseModel, Base):
  __tablename__ = 'users'
  
  id = Column(Integer, primary_key=True)
  user_id = Column(String)
  role = Column(String)
  email = Column(String(128), nullable=False)
  national_id_number = Column(Integer)
  books = relationship("Book", backref='user')

  def __init__(self, *args, **kwargs):
    """initializes user"""
    super().__init__(*args, **kwargs)

  def __setattr__(self, name, value):
    """sets a password with md5 encryption"""
    if name == "password":
        value = md5(value.encode()).hexdigest()
    super().__setattr__(name, value)