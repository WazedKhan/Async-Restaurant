import asyncio

# Constants for order status
ORDER_PLACED = "Order Placed"
ORDER_COMPLETE = "Order Complete"

# Dictionary to hold the status of multiple orders
order_status = {}


# Function to place an order and update its status
async def place_order(order_id, name, preparation_time):
    print(
        f"Order {order_id} ({name}) has been placed. Please wait {preparation_time} minutes."
    )
    order_status[order_id] = ORDER_PLACED
    await asyncio.sleep(preparation_time)  # Convert minutes to seconds
    order_status[order_id] = ORDER_COMPLETE
    print(f"Order {order_id} ({name}) is ready. Bon Appetit!")


# Function to provide complementary drinks and notify the customer
async def provide_complementary(order_id):
    await asyncio.sleep(1)
    print(
        f"Order {order_id}: Please enjoy your complementary drinks, your order will be ready shortly."
    )
    while order_status.get(order_id) != ORDER_COMPLETE:
        # Check order status periodically
        await asyncio.sleep(0.5)
        if order_status.get(order_id) != ORDER_COMPLETE:
            print(f"Order {order_id}: Please wait, your order is still being prepared.")


# Function to manage the ordering process for multiple orders
async def waiter(orders):
    tasks = []
    for order in orders:
        order_id = order["id"]
        name = order["name"]
        preparation_time = order["prepare_time"]
        place_order_task = asyncio.create_task(
            place_order(order_id, name, preparation_time)
        )
        provide_complementary_task = asyncio.create_task(
            provide_complementary(order_id)
        )
        tasks.extend([place_order_task, provide_complementary_task])
    await asyncio.gather(*tasks)


# Example order data with details
orders = [
    {"id": 1, "name": "Burger", "prepare_time": 1, "price": 5.99},
    {"id": 2, "name": "Pizza", "prepare_time": 2, "price": 8.99},
    {"id": 3, "name": "Pasta", "prepare_time": 3, "price": 7.99},
]

# Run the waiter function with the list of orders
asyncio.run(waiter(orders))
