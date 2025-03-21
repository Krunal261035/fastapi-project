from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Item(BaseModel):
    id : int | None = None
    name: str


fake_items_db = [{"id":1,"item_name": "Foo"}, {"id":2,"item_name": "Bar"}, {"id":3,"item_name": "Baz"}]

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return fake_items_db[item_id-1]

@app.put("/items/{item_id}")                    
async def update_item(item_id: int, item: Item):
    fake_items_db[item_id-1] = item
    return {"message": "Item has been updated successfully"}
