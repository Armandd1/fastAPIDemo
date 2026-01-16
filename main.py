# main.py
import logging
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

# Configure logging with timestamped format
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True


items = [
    Item(name="Sample Item 1", price=10.0, in_stock=True),
    Item(name="Sample Item 2", price=20.0, in_stock=True),
    Item(name="Sample Item 3", price=30.0, in_stock=True),
    Item(name="Sample Item 4", price=40.0, in_stock=True),
    Item(name="Sample Item 5", price=50.0, in_stock=True),
    Item(name="Sample Item 6", price=60.0, in_stock=True),
    Item(name="Sample Item 7", price=70.0, in_stock=True),
    Item(name="Sample Item 8", price=80.0, in_stock=True),
    Item(name="Sample Item 9", price=90.0, in_stock=True),
    Item(name="Sample Item 10", price=100.0, in_stock=True),
]

@app.post("/items/")
async def create_item(item: Item):
    items.append(item)
    return item

@app.get("/items/")
def get_items(skip: int = 0, limit: int = 10, in_stock: Optional[bool] = None):
    filtered_items = items
    if in_stock is not None:
        filtered_items = [item for item in items if item.in_stock == in_stock]
    return filtered_items[skip: skip + limit]

@app.get("/items/{item_id}")
async def get_item_by_id(item_id: int):
    if item_id < 0 or item_id >= len(items):
        return {"error": "Invalid item_id: out of bounds"}
    return items[item_id]

@app.get("/log")
async def log_endpoint():
    logger.info("log endpoint was called")
    return {"Message": "Endpoint with standard logging"}