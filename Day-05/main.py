from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class Item(BaseModel):
    name: str
    age: int
    discpription: str=None

@app.post("/items/")
def Create_item(item: Item):
    return{
        "message":"Successfully created", "item":item 
    }