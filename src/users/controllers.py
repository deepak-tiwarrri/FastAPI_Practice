from src.users.dtos import UserSchema
from sqlalchemy.orm import Session
import jwt
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash

def register_user(body,db:Session):
   print(body.model_dump())
   return {"status":"Registered successfully"}

