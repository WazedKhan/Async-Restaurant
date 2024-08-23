import asyncio


class OrderController:
    async def place_order(self, order_data):
        # Simulate an async operation, e.g., saving order to a database
        await asyncio.sleep(1)
        print(
            f"Order placed for Table {order_data['table_number']} with items: {', '.join(order_data['items'])}"
        )

    async def list_orders(self):
        await asyncio.sleep(1)  # Simulate async I/O
        print("Listing all orders...")
        # For demo purposes, we're just printing a message
        # You can extend this to actually list stored orders
