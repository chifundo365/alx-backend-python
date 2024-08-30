#!/usr/bin/env python3
''' Implements an asynchronous function '''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
    generates a random number between 0 and max_delay
    pauses the function execution in generated rand. # seconds

    Args:
        max_delay: the maximum number
    Returns:
        float: generated random number
    '''
    n = random.uniform(0, max_delay)
    await asyncio.sleep(n)
    return n
