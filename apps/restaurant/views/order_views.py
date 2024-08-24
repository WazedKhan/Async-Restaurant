from typing import Union

from fastapi import FastAPI, BackgroundTasks
from restaurant.utils.task_manager import simulate_order_placing
from restaurant.models.task_status import task_status

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/simulate-order-placing/{order_id}")
async def place_order(order_id: str, background_tasks: BackgroundTasks):
    # Add the task to background execution
    background_tasks.add_task(simulate_order_placing, order_id)
    # Return instant response
    return {"message": "Order received", "order_id": order_id}


@app.get("/order-status/{order_id}")
def order_status(order_id: str):
    # Retrieve the status of the order
    status = task_status.get(order_id, "Order not found")
    return {"order_id": order_id, "status": status}
