import sys
import asyncio

from time import sleep

# TODO: add create_subprocess_exec support


class Tasks:
    def __init__(self):
        self.method_list = []
        self.task_list = []
        self.results = {}

    def result(self, result_key):
        return self.results[result_key]

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
                if task.done():
                    result_key = task.get_coro().__name__

                    if result_key not in self.results:
                        self.results[task.get_coro().__name__] = task.result()
                else:
                    running_task_count += 1

            if running_task_count == 0:
                break

            await self.yield_task()

    @classmethod
    async def yield_task(self, yield_time=0.0):
        await asyncio.sleep(yield_time)


async def method_1(p):
    for i in range(40):
        print("method_1 running", p, i)

        await Tasks.yield_task()

    return "method_1_return"


async def method_2(p):
    for i in range(20):
        print("method_2 running", p, i)

        await Tasks.yield_task()


async def method_3():
    for i in range(30):
        print("method_3 running", i)

        await Tasks.yield_task()


tasks = Tasks()

tasks.create_task(method_1(999))
tasks.create_task(method_2("text"))
tasks.create_task(method_3())

tasks.run()

print("result 1", tasks.result("method_1"))
print("result 2", tasks.result("method_2"))
print("result 3", tasks.result("method_3"))
