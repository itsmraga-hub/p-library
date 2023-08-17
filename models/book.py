from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from models.base_model import BaseModel, Base


class Book(BaseModel, Base):
  __tablename__ = 'books'

  name = Column(String)
  code = Column(String)
  user_id = Column(Integer, ForeignKey('users.id'), nullable=False)