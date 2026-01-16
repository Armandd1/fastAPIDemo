from fastapi import APIRouter, HTTPException
from typing import List
from models.item import Item, Item_Response

router = APIRouter()

# Sample data for testing
items = [
    Item(id=1, name="Laptop", description="High-performance laptop", price=999.99),
    Item(id=2, name="Mouse", description="Wireless mouse", price=29.99),
    Item(id=3, name="Keyboard", price=79.99),
    Item(id=4, name="Monitor", price=149.99),
    Item(id=5, name="Headphones", price=89.99, description="Wireless headphones"),
    Item(id=6, name="Speaker", price=49.99),
    Item(id=7, name="Tablet", price=199.99),
    Item(id=8, name="Smartphone", price=699.99),
    Item(id=9, name="Camera", price=499.99),
    Item(id=10, name="Printer", price=299.99),
]


@router.get("/", response_model=List[Item_Response])
async def get_all_items():
    """Return a list of all available items"""
    return items


@router.get("/{id}", response_model=Item_Response)
async def get_item_by_id(id: int):
    """Return an item by its ID"""
    for item in items:
        if item.id == id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")
