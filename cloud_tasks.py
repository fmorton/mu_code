from birdbrain_hummingbird import BirdbrainHummingbird
from birdbrain_tasks import BirdbrainTasks

import random

async def flash(bird, port, brightness_list):
   while True:
        brightness = random.choice(brightness_list)

        bird.tri_led(port, brightness, brightness, brightness)

        await BirdbrainTasks.yield_task(random.uniform(0.1, 0.333))

        bird.tri_led(port, 0, 0, 0)

        await BirdbrainTasks.yield_task(random.uniform(0.1, 0.8))

bird = BirdbrainHummingbird('A')

brightness_list = [ 0, 0, 0, 0, 0, 20, 40, 60, 80, 100 ]

tasks = BirdbrainTasks()

tasks.create_task(flash(bird, 1, brightness_list))
tasks.create_task(flash(bird, 2, brightness_list))

tasks.run()
