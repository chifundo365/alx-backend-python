#!/usr/bin/env python3
''' Implement an asyncronous coroutine '''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    ''' Yields 10 random values after waiting for a second for each value '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
