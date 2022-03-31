from fastapi import FastAPI
from schemas.student import Student
from config.db import con
from models.index import students
app=FastAPI()

# best way to make api
@app.get('/api/students')
async def index():
    data=con.execute(students.select()).fetchall()
    return {
        "success": True,
        "data":data
    }

# insert data
@app.post('/api/students')
async def store(student:Student):
    data=con.execute(students.insert().values(
        name=student.name,
        email=student.email,
        age=student.age,
        country=student.country,
    ))

    if data.is_insert:
        return {
            "success": True,
            "msg":"Student Store Successfully"
        }
    else:
         return {
            "success": False,
            "msg":"Some Problem"
        }

# edit data
@app.patch('/api/students/{id}')
async def edit_data(id:int):
    data=con.execute(students.select().where(students.c.id==id)).fetchall()
    return {
        "success": True,
        "data":data
    }

# update data

@app.put('/api/students/{id}')
async def update(id:int,student:Student):
    data=con.execute(students.update().values(
        name=student.name,
        email=student.email,
        age=student.age,
        country=student.country,
    ).where(students.c.id==id))
    if data:
        return {
            "success": True,
            "msg":"Student Update Successfully"
        }
    else:
         return {
            "success": False,
            "msg":"Some Problem"
        }

# delete data
@app.delete('/api/students/{id}')
async def delete(id:int):
    data=con.execute(students.delete().where(students.c.id==id))
    if data:
        return {
            "success": True,
            "msg":"Student Delete Successfully"
        }
    else:
         return {
            "success": False,
            "msg":"Some Problem"
        }

# search data

@app.get('/api/students/{search}')
async def search(search):
    data=con.execute(students.select().where(students.c.name.like('%'+search+'%'))).fetchall()
    return {
        "success": True,
        "data":data
    }
