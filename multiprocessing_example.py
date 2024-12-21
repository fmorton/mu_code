from library import *


async def task_1():
    while True:
        print(datetime.datetime.now(), "task_1")
        await asyncio.sleep(random.uniform(0, 5))


async def task_2():
    for i in range(20):
        print(datetime.datetime.now(), "task_2...", i)
        await asyncio.sleep(random.uniform(0, 1))


async def task_3():
    while True:
        print(datetime.datetime.now(), "task_3")
        await asyncio.sleep(0.25)


async def runner():
    await asyncio.gather(task_1(), task_2(), task_3())


asyncio.run(runner())
