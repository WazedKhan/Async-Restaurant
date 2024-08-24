import asyncio
from restaurant.controllers.order_controller import (
    async_place_order,
    provide_complementary,
)
from restaurant.models.task_status import task_status


def simulate_order_placing(order_id: str):
    async def run_tasks():
        task_status = {}
        # Run both tasks concurrently
        place_order_task = asyncio.create_task(async_place_order(order_id, task_status))
        provide_complementary_task = asyncio.create_task(provide_complementary(order_id, task_status))

        # Wait for both tasks to complete
        await asyncio.gather(place_order_task, provide_complementary_task)

    asyncio.run(run_tasks())
