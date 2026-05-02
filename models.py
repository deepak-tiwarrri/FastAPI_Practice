from sqlalchemy import Column, Integer, String
from src.utils.db import Base

# This class = one table in the database
class User(Base):
    __tablename__ = "users"  # table name in SQLite

    id     = Column(Integer, primary_key=True, index=True)  # auto increment
    name   = Column(String, nullable=False)
    email  = Column(String, unique=True, index=True)