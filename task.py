import sys
import asyncio
import datetime
import random

from time import sleep

async def task_1():
    for i in range(60):
        print("task_1 running")

        await asyncio.sleep(0.5)

async def task_2():
    for i in range(60):
        print("task_2 running")

        await asyncio.sleep(0.5)

async def task_3():
    for i in range(60):
        print("task_3 running")

        await asyncio.sleep(0.5)


class BirdbrainTask:
    def __init__(self):
        self.tasks = []

    def create_task(self, task):
        self.tasks.append(asyncio.create_task(task))

    async def runner(bird):
        while True:
        await asyncio.sleep(0.5)

   def run(self):
        asyncio.run(runner(bird))


tasks = BirdbrainTask()

tasks.create_task(task_1())
tasks.create_task(task_2())
tasks.create_task(task_3())

'''
async def runner(bird):
    tasks = []

    tasks.append(asyncio.create_task(bitmap(bird)))
    tasks.append(asyncio.create_task(scanner(bird)))
    tasks.append(asyncio.create_task(spinner(bird)))
    tasks.append(asyncio.create_task(extra_rgb(bird)))

    all_done = False

    while True:
        running_count = 0

        for task in tasks:
            if not task.done(): running_count += 1

        if running_count == 0: break

        await asyncio.sleep(0.5)


asyncio.run(runner(bird))

bird.stopAll()
'''
