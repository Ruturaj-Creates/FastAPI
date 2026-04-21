from passlib.context import CryptContext

pw_context=CryptContext(schemes=["argon2"],deprecated="auto")

def hash_pw(password:str) ->str:
    return pw_context.hash(password)

def verify_pw(plain_password:str,hashed_password:str) ->bool:
    return pw_context.verify(plain_password,hashed_password)

