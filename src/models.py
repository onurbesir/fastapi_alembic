from sqlalchemy import Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql.schema import Column
from .database import Base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    age = Column(Integer, nullable=False)