
from fastapi import FastAPI 
from pydantic import BaseModel
from enum import Enum
import uvicorn

app = FastAPI()

# Define the Student class
class Student(BaseModel):
    id: int
    name: str
    age: int
    grade: str
    gender: Enum  # Assuming you have defined an Enum for gender

# Define the Gender enum (assuming you have already defined it)
class Gender(Enum):
    MALE = "male"
    FEMALE = "female"

# Create instances of the Student class and populate the students list
Students = [
    Student(id=1234, name="Bilal", age=32, grade="A+", gender=Gender.MALE),
    Student(id=5678, name="Humza", age=28, grade="A+", gender=Gender.MALE),
    Student(id=1213, name="xyz", age=28, grade="A+", gender=Gender.FEMALE)
]

# Query params
@app.get("/")
def home():
    return Students

@app.get("/students/{id}")
async def get_student(id:int):
    for student in Students:
        if student.id == id:
            return {
                "id": student.id,
                "name": student.name,
                "age": student.age,
                "grade": student.grade,
                "gender": student.gender.value  # Assuming gender is an Enum
            }
    else:
        return {"message": f"Student with ID {id} is not in the student list"}

# POST request to add a student
# @app.post("/students")
# async def add_student(student: Student):
#     Students.append(student)
#     return {"message": "Student added successfully"}

# Function to start the server
def start():
    uvicorn.run("todo.main:app", host="127.0.0.1", port=8080, reload=True)