#!/usr/bin/env python3
"""
a coroutine called async_generator that takes no argument
"""

from asyncio import sleep
from random import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    loops 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10
    """
    for i in range(10):
        await sleep(1)
        yield 10 * random()
