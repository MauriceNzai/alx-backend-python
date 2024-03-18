#!/usr/bin/env python3
''' Description: Import wait_random from the previous python file
                 wait_n returns the list of all the delays(float values)
                 in ascending order without using sort().
    Arguments: n: int, max_delay: int = 10
'''

import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """ Waits for ran delay until max_delay, returns list of actual delays """
    spawn_ls = []
    delay_ls = []
    for i in range(n):
      delayed_task = asyncio.create_task(wait_random(max_delay)) 
      delayed_task.add_done_callback(lambda x: delay_ls.append(x.result())) 
      spawn_ls.append(delayed_task)
  
    for spawn in spawn_ls:
      await spawn 
  
    return delay_ls
