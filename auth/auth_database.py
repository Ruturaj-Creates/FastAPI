from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
 
# Read DATABASE_URL from environment (Docker sets this)
# Fallback to localhost for local development
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:54320/FastapiDB"
)
 
engine = create_engine(DATABASE_URL)
sessionlocal = sessionmaker(autoflush=False, bind=engine)
Base = declarative_base()
 
 
def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()