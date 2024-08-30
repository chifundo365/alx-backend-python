#!/usr/bin/env python3
''' Implements a coroutine function that spawns another function '''
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    spawns wait_random n times and passes max_delay to it

    Args:
        n: number of times to spawn the wait_random processs
        max_delay: maximum delay

    Returns:
        List: containing generated float values from the coroutine function
    '''
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
