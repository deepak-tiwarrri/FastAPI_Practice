from fastapi import HTTPException, status
from src.users.dtos import UserSchema, LoginSchema
from sqlalchemy.orm import Session
import jwt
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
from src.users.models import UserModel
from src.utils.settings import Settings
from datetime import datetime, timedelta
password_helper = PasswordHash.recommended()


def get_hash_password(password):
    return password_helper.hash(password)


def verify_hash_password(plain_password, hash_password):
    return password_helper.verify(plain_password, hash_password)


def register_user(body: UserSchema, db: Session):
   existing_user = db.query(UserModel).filter(
       UserModel.username == body.username).first()
   if existing_user:
       raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                           detail="User is already registered")

   existing_email = db.query(UserModel).filter(
       UserModel.email == body.email).first()
   if existing_email:
       raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                           detail="Email is already registered")

   hashed_password = get_hash_password(body.password)

#    try:
   new_user = UserModel(
       name=body.name,
       username=body.username,
       password=hashed_password,
       email=body.email
   )

   db.add(new_user)
   db.commit()
   db.refresh(new_user)
   return new_user
#    except Exception as e:
#        db.rollback()
#        print(e)


def login_user(body: LoginSchema, db: Session):
    existing_user = db.query(UserModel).filter(
        UserModel.username == body.username).first()
    if not existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="User is not registered")
    if not verify_hash_password(body.password, existing_user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Wrong Password")

    finish_time = datetime.now() + timedelta(Settings.EXP)
    print(finish_time)

    payload = {
        "_id": existing_user.id,
        "exp": finish_time
    }
    token = jwt.encode(payload, Settings.SECRET_KEY,
                       algorithm=Settings.ALGORITHM)
    print(token)
    return {"user": existing_user, "token": token}




