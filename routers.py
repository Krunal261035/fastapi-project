from fastapi import APIRouter,Depends,Path,HTTPException
from schemas import Todo, TodoUpdate
from curd import insert_task, get_all_task, get_task, update_task, delete_task
from models import users_collection, MongoClient, get_current_database
from bson import ObjectId

router = APIRouter()

@router.post("/create")
async def create(Task_data: Todo):
    task_id = insert_task(Task_data) 
    return {"message": "created successfully", "data": str(task_id)}

@router.get("/check")
async def check_all_task(db: MongoClient = Depends(get_current_database)):
    task = get_all_task()
    return {"body":task}
@router.get("/check/{task_id}")
async def check(task_id: int, db: MongoClient = Depends(get_current_database)):
    task = get_task(task_id)
    return {"body":task}
# @router.get("/check/{task_id}")
# async def check(task_id: str, db: MongoClient = Depends(get_current_database)):
#     task = get_task(task_id)
#     return task

@router.put("/update/{task_id}")
async def update(task_id: int, Task_data: TodoUpdate, db: MongoClient = Depends(get_current_database)):
    task = update_task(Task_data, task_id)
    return{"body":task} 

@router.delete("/delete/{task_id}")
async def delete(task_id: int, db: MongoClient = Depends(get_current_database)):
    task = delete_task(task_id)
    return {"body":task}




