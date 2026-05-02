# used to define the schema of the model

from pydantic import BaseModel

class UserSchema(BaseModel):
   id:int
   name:str
   username= str
   password = str
   email = str
   
