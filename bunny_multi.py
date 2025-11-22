import random

from robot.hummingbird import Hummingbird
from tasks import Tasks

CACHE_LIGHT_LEVEL = "cache_light_level"
LIGHT_CUTOFF_LEVEL = 7
TASK_WAIT = 0.1
EARS_WAIT = 0.25


def light_sensor_covered(bird):
    return bird.get_cache(CACHE_LIGHT_LEVEL) <= LIGHT_CUTOFF_LEVEL


def random_event():
    return random.random() < 0.1


def r(maximum):
    return random.randint(0, maximum)


async def set_light_level(bird):
    while True:
        bird.set_cache(CACHE_LIGHT_LEVEL, bird.light(1))

        await Tasks.yield_task(TASK_WAIT)


async def ears(bird):
    while True:
        while light_sensor_covered(bird):
            bird.position_servo(1, 90)
            bird.position_servo(2, 90)

            await Tasks.yield_task(EARS_WAIT)

            bird.position_servo(1, 120)
            bird.position_servo(2, 60)

            await Tasks.yield_task(EARS_WAIT)

        bird.position_servo(1, 90)
        bird.position_servo(2, 90)

        if random_event():
            bird.position_servo(1, 100)

        await Tasks.yield_task(TASK_WAIT)


async def eyes(bird):
    while True:
        while light_sensor_covered(bird):
            bird.led(1, 80)
            bird.led(2, 80)

            await Tasks.yield_task(TASK_WAIT)

        bird.led(1, 2)
        bird.led(2, 4)

        await Tasks.yield_task(TASK_WAIT)


async def nose(bird):
    while True:
        while light_sensor_covered(bird):
            bird.tri_led(1, r(100), r(100), r(100))

            await Tasks.yield_task(TASK_WAIT)

        bird.tri_led(1, r(3), r(3), r(7))

        await Tasks.yield_task(TASK_WAIT)


bird = Hummingbird("A")

tasks = Tasks()

tasks.create_task(set_light_level(bird))
tasks.create_task(ears(bird))
tasks.create_task(eyes(bird))
tasks.create_task(nose(bird))

tasks.run()
