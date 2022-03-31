from pydantic import BaseModel

class Student(BaseModel):
    name:str
    email:str
    age:int
    country:str