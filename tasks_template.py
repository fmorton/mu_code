from birdbrain import Hummingbird
from birdbrain import Tasks


async def task_1(bird):
    while True:
        print("task_1 running")

        await Tasks.yield_task(1.0)


async def task_2(bird):
    while True:
        print("task_2 running")

        await Tasks.yield_task(0.5)


bird = Hummingbird("A")

tasks = Tasks()

tasks.create_task(task_1(bird))
tasks.create_task(task_2(bird))

tasks.run()
