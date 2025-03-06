import sys
import asyncio
import datetime
import random

from BirdBrain import Hummingbird
from time import sleep

async def task_1_method(bird):
    while True:
        print("Task 1")
        await asyncio.sleep(random.uniform(0, 5))

async def task_2_method(bird):
    while True:
        print("Task 2")
        await asyncio.sleep(random.uniform(0, 5))

class BirdbrainRunner():
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        pass

    #async def run_tasks(bird):
    async def run_tasks(self):
        runner_tasks = []

        for task in self.tasks:
            print("TASK",task)
            await asyncio.sleep(0.25)

        #runner_tasks.append(

    pass


bird = Hummingbird("A")

runner = BirdbrainRunner()

#task_1 = asyncio.create_task(task_1_method(bird))
task_1 = task_1_method(bird)
task_2 = task_2_method(bird)

runner.add_task(task_1)
runner.add_task(task_2)

runner.run_tasks()

#async def runner(bird):
#    task_1 = asyncio.create_task(task_1_method(bird))
#    task_2 = asyncio.create_task(task_2_method(bird))

#    tasks = [ task_1, task_2 ]

    ###await asyncio.gather(task_1_method(bird), task_2_method(bird))
#    await asyncio.gather(*tasks)


#bird = Hummingbird("A")

#asyncio.run(runner(bird))
