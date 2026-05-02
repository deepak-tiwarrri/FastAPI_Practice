from sqlalchemy import String,Boolean,Integer,Boolean,Column
from src.utils.db import Base

class TaskModel(Base):
   __tablename__ = "user_task"

   id = Column(Integer,primary_key=True)
   title = Column(String)
   description = Column(String)
   is_completed = Column(Boolean,default=False)
