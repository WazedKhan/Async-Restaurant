import asyncio


async def async_place_order(order_id: str, task_status: dict):
    order_prepare_time = 3
    print(f"Placing order {order_id}...")  # Debug statement
    print(f"Order will prepared in {order_prepare_time} min")
    await asyncio.sleep(order_prepare_time)  # Simulate delay
    task_status[order_id] = "Order ready"  # Update status
    print(f"Order {order_id} placed.")  # Debug statement
    return {"status": "Order ready", "message": "Bon Appetit"}


async def provide_complementary(order_id: str, task_status: dict):
    print(f"Providing complementary drinks for order {order_id}...")  # Debug statement
    # Wait until the order is ready
    while task_status.get(order_id) != "Order ready":
        await asyncio.sleep(0.1)  # Check status periodically
    await asyncio.sleep(1)  # Simulate delay
    task_status[order_id] = "Drinks served"  # Update status
    print(f"Drinks served for order {order_id}.")  # Debug statement
    return {
        "status": "Drinks served",
        "message": "Please enjoy your complementary drinks",
    }
