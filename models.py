from pydantic import BaseModel


class Student(BaseModel):
    id: int
    name: str


class Task(BaseModel):
    id: int
    title: str
    student_id: int
    completed: bool = False