from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

url="postgresql://postgres:postgres@localhost:54320/FastapiDB"
engine=create_engine(url)
sessionlocal=sessionmaker(autoflush=False,bind=engine)
Base=declarative_base()

def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()

