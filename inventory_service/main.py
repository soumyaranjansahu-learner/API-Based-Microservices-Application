from fastapi import FastAPI

app = FastAPI()

# Mock database: item_id -> {details}
inventory = {
    "1": {"name": "Microchip", "price": 50, "stock": 100},
    "2": {"name": "Sensor", "price": 25, "stock": 200}
}

@app.get("/items/{item_id}")
def get_item(item_id: str):
    return inventory.get(item_id, {"error": "Item not found"})