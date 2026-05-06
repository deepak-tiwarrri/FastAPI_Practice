from fastapi import HTTPException
from src.tasks.models import TaskModel
from sqlalchemy.orm import Session 
from src.users.models import UserModel

def create_task(body,db:Session,current_user:UserModel):
   data = body.model_dump()
   new_task = TaskModel(
      title=data['title'],
      description=data['description'],
      is_completed=data['is_completed'],
      user_id=current_user.id
   )
   db.add(new_task)
   db.commit()
   db.refresh(new_task)

   return {"task":new_task,"user":current_user}


def get_task(db:Session):
   tasks = db.query(TaskModel).all()
   return tasks

def get_one_task(task_id:int,db:Session):
   single_task = db.query(TaskModel).get(task_id)
   if not single_task:
      raise HTTPException(status_code=404,detail="Task id not found")
   return {"status":"Task fetched: !!","task":single_task}
   


def update_task(body,task_id:int,db:Session):
   task = db.query(TaskModel).get(task_id)
   if not task:
      raise HTTPException(status_code=404,detail="Task ID is incorrect")
   body_data = body.model_dump()
   for field,value in body_data.items():
      setattr(task,field,value)
   
   db.add(task)
   db.commit()
   db.refresh(task)
   return {"status": "Task updated successfully", "data": task}


def delete_task(task_id:int,db:Session):
   task = db.query(TaskModel).get(task_id)
   if not task:
      raise HTTPException(status_code=404,detail='Task not found')
   db.delete(task)
   db.commit()

   return None
