from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Iteam(BaseModel):
    name: str
    description: str=None
    age: int

@app.get("/iteams")
def get_iteams(iteam: Iteam):
    return {
        "message": "Iteam retrieved successfully",
        "iteam": iteam
    }
