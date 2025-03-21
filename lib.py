from fastapi import FastAPI,Depends,Path,HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId

app = FastAPI()

uri = "mongodb://localhost/library"
client = MongoClient(uri)
database = client.get_database()

users_collection = database['Books']

class Books(BaseModel):
    title: str
    author : str
    price: int

async def get_current_database():
    db = database
    yield db

@app.post("/insert_book")
async def insert(book_data:Books):
    books_id = insert_data(book_data)
    return {"message":"added successfully","books": str(books_id)}


def insert_data(book_data):
    book_dict = book_data.dict()
    result = users_collection.insert_one(book_dict)
    return result.inserted_id


@app.get("/Read_book")
async def get_books(db: MongoClient = Depends(get_current_database)):
    book = users_collection.find()
    book_list = []
    for books in book:
        books['_id'] = str(books['_id'])
        book_list.append(books)
    return book_list

@app.get("/Read_book/{book_id}")
async def get(book_id: str = Path(...),db: MongoClient = Depends(get_current_database)):
    book = users_collection.find_one({"_id": ObjectId(book_id)})
    if book:
        book["_id"]= str(book["_id"])
        return book
    else:
        raise HTTPException (status_code=404,detail = "user not found")

@app.put("/Read_book/{book_id}")
async def update_book(book_data:Books,book_id:str = Path(...),db: MongoClient = Depends(get_current_database)):
    book_dict = book_data.model_dump()
    book_obj_id = ObjectId(book_id)
    result = users_collection.update_one({"_id":book_obj_id},{'$set':book_dict})
    if result.modified_count ==1:
        return {"Book updated successfully"}
    else:
        raise HTTPException(status_code=404,detail="book not found")
    
@app.delete("/Read_book/{book_id}")
async def delete_book(book_id:str = Path(...),db: MongoClient = Depends(get_current_database)):
    result = users_collection.delete_one({"_id":ObjectId(book_id)})
    if result.deleted_count ==1:
        return {"Book deleted successfully"}
    else:
        raise HTTPException(status_code=404,detail="book not found")
    
