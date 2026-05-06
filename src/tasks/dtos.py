from pydantic import BaseModel
from src.users.dtos import UserResponseSchema

class TaskSchema(BaseModel):
   title:str
   description:str
   is_completed:bool = False


class TaskResponseSchema(BaseModel):
   id:int
   title:str
   description:str
   is_completed:bool


class TaskCreateResponseSchema(BaseModel):
   task: TaskResponseSchema
   user: UserResponseSchema




