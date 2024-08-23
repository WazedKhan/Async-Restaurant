from controllers.order_controller import OrderController
import asyncio


class OrderView:
    def __init__(self):
        self.controller = OrderController()

    async def display_menu(self):
        while True:
            print("1. Place Order")
            print("2. List Orders")
            print("3. Exit")
            choice = input("Select an option: ")
            if choice == "1":
                await self.place_order()
            elif choice == "2":
                await self.list_orders()
            elif choice == "3":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    async def place_order(self):
        table_number = input("Enter table number: ")
        items = input("Enter items (comma-separated): ").split(",")
        order_data = {"table_number": table_number, "items": items}
        await self.controller.place_order(order_data)

    async def list_orders(self):
        await self.controller.list_orders()
