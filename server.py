from fastapi import FastAPI
from pydantic import BaseModel
from revolver import *
from servmot import sweep
class Item(BaseModel):
    id: int

app = FastAPI()

@app.get("/")
def index():
    return {"response": "the application in running"}


@app.post("/spin")
async def perfume(item: Item):
	try:
		id = item.id
		revolver(id)
		sweep(30)
	except Exception as e:
		return { "error": str(e) }
	return { "response": f"This is the id: {id}" }
