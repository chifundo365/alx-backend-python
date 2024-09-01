#!/usr/bin/env python3
''' Implements a coroutine that runs tasks in parallel '''
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    ''' Measure the runtime of running a couritine 4 times '''
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end_time = time.time()

    return end_time - start_time
