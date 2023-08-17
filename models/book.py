from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
import uuid
from sqlalchemy.orm import declarative_base
from models.base_model import BaseModel, Base


class Book(BaseModel, Base):
  __tablename__ = 'books'

  name = Column(String)
  code = Column(String)
  user_id = Column(String(60), ForeignKey('users.id'), nullable=False)