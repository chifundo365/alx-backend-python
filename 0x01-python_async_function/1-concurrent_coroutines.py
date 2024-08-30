#!/usr/bin/env python3
''' Implements a coroutine function that spawns another function '''
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    spawns wait_random n times and passes max_delay to it

    Args:
        n: number of times to spawn the wait_random processs
        max_delay: maximum delay

    Returns:
        List: containing gnerated float values from the coroutine function
    '''
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
