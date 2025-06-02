from typing import Optional
from fastapi import FastAPI, , HTTPException, status
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
    try:
        # Simuler une vérification de disponibilité du service
        if not tasks:  # Si la liste est vide (simulation d'erreur)
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Service temporarily unavailable"
            )
            
        return tasks
        
    except HTTPException as http_exc:
        # On relance les HTTPException telles quelles
        raise http_exc
        
    except Exception as e:
        logger.error(f"Unexpected error in read_tasks: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred while processing your request"
        )

@app.post("/tasks")
async def create_task(task: Task):
    new_task = task.dict()
    new_task["id"] = len(tasks) + 1
    tasks.append(new_task)  # Ajouter le dictionnaire à la liste
    return new_task
