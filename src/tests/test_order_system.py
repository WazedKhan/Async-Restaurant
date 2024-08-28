import asyncio
import pytest
from src.restaurant import (
    place_order,
    provide_complementary,
    order_status,
    ORDER_PLACED,
    ORDER_COMPLETE,
)


@pytest.mark.asyncio
async def test_place_order():
    order_id = 1
    name = "Burger"
    preparation_time = 1  # seconds for testing

    # Run place_order in a task
    await place_order(order_id, name, preparation_time)

    assert order_status.get(order_id) == ORDER_COMPLETE


@pytest.mark.asyncio
async def test_provide_complementary():
    order_id = 1

    # Initialize the order status to be placed
    order_status[order_id] = ORDER_PLACED

    # Run provide_complementary in a task
    complementary_task = asyncio.create_task(provide_complementary(order_id))

    # Simulate the order being completed
    order_status[order_id] = ORDER_COMPLETE

    # Wait for the complementary task to complete
    await complementary_task

    assert order_status.get(order_id) == ORDER_COMPLETE
