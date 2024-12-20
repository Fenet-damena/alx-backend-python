#!/usr/bin/env python3
"""rand.py"""

import random
import asyncio


# ANSI Color
c = (
    "\033[0m", # end of color
    "\033[36m", # Cyan
    "\033[91m", # Red
    "\033[35m" # Margenta
)

async def makeRandom(idx: int, threshold: int = 6) -> int:
    print(c[idx+1] + f"Initiated makerandom ({idx}).")
    
    i = random.randint(0, 10)

    while i <= threshold:
        print(c[idx+1] + f"makerandom {idx} == {i} too low; retrying.")
        await asyncio.sleep(idx+1)
        i = random.randint(0, 10)
    print(c[idx + 1] + f"---> Finished: makerandom({idx}) == {i}" + c[0])
    return i
    
async def main():
    res =  await asyncio.gather(*(makeRandom(i, 10 - i - 1) for i in range(3)))
    return res
    
if __name__ == '__main__':
    random.seed(400)
    r1, r2, r3 = asyncio.run(main())
    print()
    print(f"r1: {r1}, r2: {r2}, r3: {r3}")