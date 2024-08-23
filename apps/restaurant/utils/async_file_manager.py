# async_file_manager.py

import asyncio


async def read_file(file_path):
    await asyncio.sleep(0.5)  # Simulate async I/O operation
    with open(file_path, "r") as file:
        return file.read()


async def write_file(file_path, content):
    await asyncio.sleep(0.5)  # Simulate async I/O operation
    with open(file_path, "w") as file:
        file.write(content)
