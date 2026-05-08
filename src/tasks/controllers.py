from fastapi import HTTPException,status
from src.tasks.models import TaskModel
from sqlalchemy.orm import Session 
from src.users.models import UserModel

def create_task(body,db:Session,current_user:UserModel):
   data = body.model_dump()
   new_task = TaskModel(
      title=data['title'],
      description=data['description'],
      is_completed = data['is_completed'],
      user_id = current_user.id
   )
   db.add(new_task)
   db.commit()
   db.refresh(new_task)
   return {"task":new_task,"user":current_user}


def get_task(db:Session,user:UserModel):
   tasks = db.query(TaskModel).filter(TaskModel.user_id == user.id).all()
   return tasks

def get_one_task(task_id:int,db:Session,user:UserModel):
   single_task = db.query(TaskModel).filter(TaskModel.id == task_id, TaskModel.user_id == user.id).first()
   if not single_task:
      raise HTTPException(status_code=404,detail="Task id not found")
   return {"status":"Task fetched: !!","task":single_task}
   


def update_task(body,task_id:int,db:Session,user:UserModel):
   task:TaskModel = db.query(TaskModel).get(task_id)
   if not task:
      raise HTTPException(status_code=404,detail="Task ID is incorrect")
   
   if task.user_id != user.id: 
      raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="You are not authorized to update this task")

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
