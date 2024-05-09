from fastapi import APIRouter, HTTPException, Depends
from typing import Dict, List
from uuid import UUID, uuid4
from classes.schema_dto import Task, TaskNoId, User

router = APIRouter()

# Stockage temporaire des tâches en mémoire
tasks_db: Dict[str, Task] = {}

# CRUD API pour les tâches
@router.post("/todos/", response_model=Task)
def create_todo(task: TaskNoId):
    task_id = str(uuid4())
    tasks_db[task_id] = Task(**task.dict(), id=task_id)
    return tasks_db[task_id]

@router.get("/todos/", response_model=List[Task])
def read_todos():
    return list(tasks_db.values())

@router.get("/todos/{task_id}", response_model=Task)
def read_todo(task_id: str):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Tâche non trouvée")
    return tasks_db[task_id]

@router.patch("/todos/{task_id}", response_model=Task)
def update_todo(task_id: str, task_update: TaskNoId):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Tâche non trouvée")
    tasks_db[task_id].title = task_update.title
    return tasks_db[task_id]

@router.delete("/todos/{task_id}")
def delete_todo(task_id: str):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Tâche non trouvée")
    del tasks_db[task_id]
    return {"message": "Tâche supprimée"}
