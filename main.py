from fastapi import FastAPI
from src.utils.db import Base, engine
from src.tasks.router import task_router
from src.users.router import user_router

app = FastAPI(title="My Task Management Application", debug=True)

# Create all tables in the database
Base.metadata.create_all(bind=engine)


app.include_router(task_router)
app.include_router(user_router)














# # ──────────────────────────────────────────
# # CREATE a user
# # ──────────────────────────────────────────
# @app.post("/users/", response_model=schemas.UserResponse)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = models.User(name=user.name, email=user.email)
#     db.add(db_user)      # add to session
#     db.commit()          # save to database
#     db.refresh(db_user)  # get updated data (like auto id)
#     return db_user

# # ──────────────────────────────────────────
# # GET all users
# # ──────────────────────────────────────────
# @app.get("/users/", response_model=list[schemas.UserResponse])
# def get_all_users(db: Session = Depends(get_db)):
#     return db.query(models.User).all()

# # ──────────────────────────────────────────
# # GET single user by ID
# # ──────────────────────────────────────────
# @app.get("/users/{user_id}", response_model=schemas.UserResponse)
# def get_user(user_id: int, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == user_id).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user

# # ──────────────────────────────────────────
# # DELETE a user
# # ──────────────────────────────────────────
# @app.delete("/users/{user_id}")
# def delete_user(user_id: int, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == user_id).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     db.delete(user)
#     db.commit()
#     return {"message": "User deleted successfully"}