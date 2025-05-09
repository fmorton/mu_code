import sys
import asyncio

from time import sleep

#TODO: add create_subprocess_exec support

class BirdbrainTasks:
    def __init__(self):
        self.method_list = []
        self.task_list = []
        self.results = {}


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
                try:
                    self.results[task.get_coro().__name__] = task.result()
                except asyncio.exceptions.InvalidStateError:
                    pass

                if not task.done(): running_task_count += 1

            if running_task_count == 0: break

            await self.yield_task()

    @classmethod
    async def yield_task(self, yield_time = 0.0):
        await asyncio.sleep(yield_time)


async def method_1(p):
    for i in range(40):
        print("method_1 running", p, i)

        await BirdbrainTasks.yield_task()

    return("method_1_return")

async def method_2(p):
    for i in range(20):
        print("method_2 running", p, i)

        await BirdbrainTasks.yield_task()

async def method_3():
    for i in range(30):
        print("method_3 running", i)

        await BirdbrainTasks.yield_task()

tasks = BirdbrainTasks()

tasks.create_task(method_1(999))
tasks.create_task(method_2("text"))
tasks.create_task(method_3())

tasks.run()

print("final results", tasks.results)

