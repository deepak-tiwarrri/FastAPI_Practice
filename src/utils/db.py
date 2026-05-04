from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker,declarative_base
from src.utils.settings import settings

engine = create_engine(settings.DB_CONNECTION)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# create a base class for models
Base = declarative_base()
# dependency to get a DB session for routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()