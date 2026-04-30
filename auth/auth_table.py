from auth.auth_database import Base, engine
# import model              # for Book
from auth import models   # for User ✅ IMPORTANT

Base.metadata.create_all(bind=engine)

