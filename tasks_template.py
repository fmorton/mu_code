from birdbrain_hummingbird import BirdbrainHummingbird
from birdbrain_tasks import BirdbrainTasks

async def task_1(bird):
   while True:
        print("task_1 running")

        await BirdbrainTasks.yield_task(1.0)

async def task_2(bird):
   while True:
        print("task_2 running")

        await BirdbrainTasks.yield_task(0.5)

bird = BirdbrainHummingbird('A')

tasks = BirdbrainTasks()

tasks.create_task(task_1(bird))
tasks.create_task(task_2(bird))

tasks.run()
