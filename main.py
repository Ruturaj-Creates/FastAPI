from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()

@app.get("/")
def read_root():
    return {'message':'hello world from ruturaj'}

@app.get("/greet")
def bombastic():
    return {"Jarvis":"Good day sir"}

@app.get("/greet/{name}")
def greet(name:str):
    return {'message':f"hello {name} ji"}

@app.get("/meet/{nav}")
def greet_name_age(nav:str,age:int):
                   return {"message":f"hello {nav} and your age is {age}"}

class Student(BaseModel):
        name:str
        age:int 
        roll_no:int
    
@app.post("/create_student")
def create_student(student:Student):
        return{
                "name":student.name,
                "age":student.age,
                "role_number":student.roll_no
        }