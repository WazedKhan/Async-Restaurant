import asyncio


async def place_order():
    print("You order has been placed please wait 30 min")
    await asyncio.sleep(2)
    print("Bon Appetit")


async def provide_complementary():
    await asyncio.sleep(1)
    print("Please enjoy your complementary drinks, your order will be ready in 15 min")


async def waiter():
    place_order_task = asyncio.create_task(place_order())
    provide_complementary_task = asyncio.create_task(provide_complementary())
    await asyncio.gather(place_order_task, provide_complementary_task)


asyncio.run(waiter())
