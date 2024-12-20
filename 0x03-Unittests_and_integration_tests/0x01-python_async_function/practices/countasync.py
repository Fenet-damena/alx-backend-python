#!/usr/bin/env python3
"""countasync.py"""

import asyncio


async def countAsync():
    print("One")
    await asyncio.sleep(1)
    print("Two")
    return 1


async def mainAsync():
    
    res = await asyncio.gather(countAsync(), countAsync(), countAsync())
    # res = await asyncio.gather(*(countAsync() for _ in range(3)))
    print(res)
    
"""
def countSync():
    print("One")
    time.sleep(1)
    print("Two")
    
def mainSync():
    for i in range(3):
        countSync()

"""
if __name__ == '__main__':
    import time
    
    file  = ''.join(__file__.split('/')[-1:])
    
    s = time.perf_counter()
    asyncio.run(mainAsync())
    elapsed = time.perf_counter() - s
    print(f"{file} executed in {elapsed:.2f} seconds")
    
    
    # s2 = time.perf_counter()
    # mainSync()
    # elas = time.perf_counter() -  s2
    # print(f"{file} executed in {elas:.2f} seconds")
    
    