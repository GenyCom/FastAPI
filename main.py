from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: str

tasks = [
    {"title": "Task1",
    "description": "Description de la Task1"},
    {"title": "Task2",
    "description": "Description de la Task2"},
    ]

@app.get("/tasks")
async def read_tasks():
    return tasks

@app.post("/tasks")
async def create_task(task: Task):
    new_task = task.dict()
    new_task["id"] = len(tasks) + 1
    tasks.append(new_task)  # Ajouter le dictionnaire à la liste
    return new_task