#!/usr/bin/env python3
"""
This module defines an asynchronous routine that runs multiple
wait_random coroutines concurrently and
returns the delays in order of completion.
"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Spawns wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay value for wait_random.

    Returns:
        List[float]: A list of all the delays in
        ascending order of completion.
    """
    return asyncio.create_task(wait_random(max_delay))
