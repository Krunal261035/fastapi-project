from schemas import Todo, TodoUpdate
from models import get_current_database, users_collection
from bson import ObjectId
from fastapi import HTTPException,Depends,Path
from pymongo import MongoClient   

def insert_task(Task_data):
    Task_dict = Task_data.dict()
    result = users_collection.insert_one(Task_dict)
    return result.inserted_id

def get_all_task(db: MongoClient = Depends(get_current_database)):
    task = list(users_collection.find({},{"_id":0}))
    # task = users_collection.find()
    # task_list = []
    # for tasks in task:
    #     tasks['_id'] = str(tasks['_id'])
    #     task_list.append(tasks)
    return task

def get_task(task_id):
    task = users_collection.find_one({"id": int(task_id)})
    if task:
        task['_id'] = str(task['_id'])
        return task
    else:
        raise HTTPException(status_code=404, detail="task not found")

def update_task(Task_data: TodoUpdate, task_id: int, db: MongoClient = Depends(get_current_database)):
    task_dict = Task_data.dict()
    task_id = int(task_id)
    result = users_collection.update_one({"id": task_id}, {'$set': task_dict})
    if result.modified_count == 1:
        return {"Task updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="task not found")           

def delete_task(task_id: int, db: MongoClient = Depends(get_current_database)):
    task_id = int(task_id)
    result = users_collection.delete_one({"id": task_id})
    if result.deleted_count == 1:
        return {"Task deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="task not found")   