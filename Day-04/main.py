from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
    return{"message": "Hello Achyuth! Welcome to FastAPI"}

@app.get("/about")
def about():
    return{"message": "about AutoMachine"}

@app.get("/hello/{name}")
def hello(name):
    return{"message":f"Hello! {name}"}

@app.get("/square/{num}")
def square(num: int):
    return{"square": num * num}

@app.get("/workflow_id/{id}")
def workflow_id(id:int):
    return{"workflow_id": id}
