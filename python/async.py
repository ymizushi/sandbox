#!/usr/bin/env python3

import asyncio


loop = asyncio.get_event_loop()

async def post():
    await asyncio.sleep(1)
    return 200

async def get():
    await asyncio.sleep(2)
    return 200


async def get_and_post():
    get_result = await get()
    print("A")
    post_result = await post()
    print("B")
    print(get_result)
    print(post_result)

def loop_x(list):
    for i in list:
        print(i)
        yield i

def loop(list):
    for i in list:
        yield from loop_x(i)


for i in foo():
    print(i)

# asyncio.ensure_future(get_and_post())
# loop.run_until_complete(get_and_post())
