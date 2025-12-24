from fastapi import FastAPI
import httpx # This library allows services to talk to each other

app = FastAPI()

INVENTORY_URL = "http://127.0.0.1:8000"

@app.post("/place-order/{item_id}")
async def place_order(item_id: str, quantity: int):
    # Call the Inventory Service
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{INVENTORY_URL}/items/{item_id}")
        item_data = response.json()

    if "error" in item_data:
        return {"status": "Rejected", "message": "Item does not exist"}

    total = item_data["price"] * quantity
    return {
        "status": "Success",
        "item": item_data["name"],
        "total_cost": total
    }