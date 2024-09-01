#!/usr/bin/env python3
''' Implements a couritine function that delas with a couritine task '''
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    ''' Correts 10 random values from another function '''
    return [i async for i in async_generator()]
