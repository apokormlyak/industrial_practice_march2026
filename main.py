from fastapi import FastAPI
from models import Student, Task
from storage import students, tasks

app = FastAPI()


@app.post("/students")
def create_student(student: Student):
    students.append(student)
    return {"message": "Студент добавлен", "student": student}


@app.get("/students")
def get_students():
    return students


@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return {"message": "Создано новое задание", "task": task}


@app.get("/tasks")
def get_tasks():
    return tasks


@app.post("/tasks/complete/{task_id}")
def complete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            return {"message": "Задание выполнено", "task": task}

    return {"error": "Задание не найдено"}
