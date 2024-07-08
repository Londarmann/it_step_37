from fastapi import FastAPI, HTTPException

from app.crud import creat_item, get_items, get_item_by_id
from app.dependencies import get_database
from app.schemas import ItemRead, ItemCreate

app = FastAPI()


@app.post("/items/", response_model=ItemRead)
async def create_new_item(item: ItemCreate):
    return await creat_item(item)


@app.get("/", response_model=list[ItemRead])
async def read_all_items():
    return await get_items()


@app.get("/{item_id}", response_model=ItemRead)
async def read_one_item(item_id: int):
    item = await get_item_by_id(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item



get_database(app)