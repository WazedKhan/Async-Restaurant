import asyncio
from apps.restaurant.views.order_view import OrderView


async def main():
    order_view = OrderView()
    await order_view.display_menu()


if __name__ == "__main__":
    asyncio.run(main())
