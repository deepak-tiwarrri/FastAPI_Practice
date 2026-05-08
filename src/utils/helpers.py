from sqlalchemy.orm import Session
from src.utils.settings import settings
from fastapi import HTTPException,status,Request,Depends
from src.users.models import UserModel
from src.utils.db import get_db
import jwt
from jwt.exceptions import InvalidTokenError

def is_authenticated(request: Request, db: Session=Depends(get_db)):

    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail="Could not validate credentials")

    token = request.headers.get('Authorization')
    print("token: ", token)

    if not token:
        raise credentials_exception

    try:
        actual_token = token.strip().split(" ")[-1].strip()
        print("actual token:", actual_token)
        payload = jwt.decode(
            actual_token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])

        print("payload: ", payload)
        print("getting the user id: ", payload.get('id'))
        user_id = payload.get('id')
        user = db.query(UserModel).filter(UserModel.id == user_id).first()
        print("user:", user)
        if not user:
            raise credentials_exception
        return user

    except InvalidTokenError:
        raise credentials_exception
