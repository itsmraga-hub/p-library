from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
from models.base_model import BaseModel, Base


class Category(BaseModel, Base):
  __tablename__ = 'categories'

  category_name = Column(String)
  category_number = Column(Integer)  