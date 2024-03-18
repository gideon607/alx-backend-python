#!/usr/bin/env python3
'''
    Async.
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for 0 and max_delay (included and float value)
    Seconds and eventually returns it.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
