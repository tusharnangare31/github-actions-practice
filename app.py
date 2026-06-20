from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Initialize the core FastAPI application instance
app = FastAPI(title="Sample Inventory API")

# Define a Pydantic data model for strict request body validation
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

# In-memory database simulation
inventory = {
    1: {"name": "Laptop", "price": 999.99, "is_offer": True}
}

# 1. Root Route (Basic GET request)
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Sample Application"}

# 2. Path & Query Parameters Route (GET request)
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item not found")
    
    item_data = inventory[item_id]
    return {"item_id": item_id, "data": item_data, "query_param": q}

# 3. Request Body Route (POST request)
@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        raise HTTPException(status_code=400, detail="Item already exists")
    
    # Store the item directly using the validated Pydantic model
    inventory[item_id] = item.model_dump()
    return {"message": "Item successfully created", "item_id": item_id, "data": inventory[item_id]}
