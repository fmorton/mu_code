import sys
import asyncio

from time import sleep


class BirdbrainTasks:
    def __init__(self):
        self.method_list = []
        self.task_list = []

    def create_task(self, method):
        self.method_list.append(method)

    def run(self):
        asyncio.run(self.runner())

    async def runner(self):
        for method in self.method_list:
            self.task_list.append(asyncio.create_task(method))

        while True:
            running_task_count = 0

            for task in self.task_list:
                if not task.done(): running_task_count += 1

            if running_task_count == 0: break

            await asyncio.sleep(0.1)


async def method_1(p):
    for i in range(10):
        print("method_1 running", p, i)

        await asyncio.sleep(0.1)

async def method_2(p):
    for i in range(20):
        print("method_2 running", p, i)

        await asyncio.sleep(0.1)

async def method_3():
    for i in range(30):
        print("method_3 running", i)

        await asyncio.sleep(0.1)

tasks = BirdbrainTasks()

tasks.create_task(method_1(999))
tasks.create_task(method_2("parameter value"))
tasks.create_task(method_3())

tasks.run()
