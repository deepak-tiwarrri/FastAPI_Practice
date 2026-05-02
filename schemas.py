from pydantic import BaseModel

# What user sends when creating
class UserCreate(BaseModel):
    name: str
    email: str

# What API sends back in response
class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True  # Converts SQLAlchemy object → JSON