import asyncio
import random

from birdbrain import Hummingbird


async def flash(bird, port, brightness_list):
    while True:
        brightness = random.choice(brightness_list)

        bird.tri_led(port, brightness, brightness, brightness)

        await asyncio.sleep(random.uniform(0.1, 0.333))

        bird.tri_led(port, 0, 0, 0)

        await asyncio.sleep(random.uniform(0.1, 0.8))


async def runner(bird):
    brightness_list = [0, 0, 0, 0, 0, 20, 40, 60, 80, 100]

    await asyncio.gather(
        flash(bird, 1, brightness_list), flash(bird, 2, brightness_list)
    )


bird = Hummingbird("A")

asyncio.run(runner(bird))
