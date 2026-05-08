from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from src.tasks.dtos import TaskSchema, TaskCreateResponseSchema
from src.tasks import controllers
from src.utils.db import get_db
from typing import List
from src.tasks.dtos import TaskResponseSchema
from src.utils.helpers import is_authenticated
from src.users.models import UserModel


# prefix means all the routes here start with /task
task_router = APIRouter(prefix='/task')

# CREATE - use 201 created
@task_router.post('/create_task',status_code=status.HTTP_201_CREATED,response_model=TaskCreateResponseSchema)
def create_task_endpoint(body:TaskSchema,db:Session=Depends(get_db),current_user:UserModel=Depends(is_authenticated)):
   return controllers.create_task(body,db,current_user)

# get all - use 200 OK and return a list
@task_router.get("/get_all_tasks",status_code=status.HTTP_200_OK,response_model=List[TaskResponseSchema])
def get_all_task_endpoint(db:Session=Depends(get_db),user:UserModel=Depends(is_authenticated)):
   return controllers.get_task(db,user)

# get one task - use 200 OK and return single task


@task_router.get('/get_task/{task_id}', status_code=status.HTTP_200_OK)
def get_one_task_endpoint(task_id:int,db:Session=Depends(get_db),user:UserModel=Depends(is_authenticated)):
   return controllers.get_one_task(task_id,db,user)


# update the task - use 200 OK and return single task
@task_router.put('/update_task/{task_id}', status_code=status.HTTP_200_OK)
def update_one_task_endpoint(body:TaskSchema,task_id:int,db:Session=Depends(get_db),user:UserModel=Depends(is_authenticated)):
   return controllers.update_task(body,task_id,db,user)


# delete the task - use 204 No Content
@task_router.delete('/delete_task/{task_id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_one_task_endpoint(task_id:int,db:Session=Depends(get_db),user:UserModel=Depends(is_authenticated)):
   return controllers.delete_task(task_id,db)

