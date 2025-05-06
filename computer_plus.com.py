from library import *

bird = BirdbrainHummingbird("A")

async def bitmap(bird):
    while True:
        a = [random.randint(0, 1) for i in range(25)]
        bird.display(a)

        bird.play_note(random.randint(32, 120), 0.025)
        sleep(random.uniform(0, 0.1))

        await asyncio.sleep(random.uniform(0, 0.01))


def scanner_leds(bird, n):
    bird.setLED(1, 0)
    bird.setLED(2, 0)
    bird.setLED(3, 0)
    bird.setTriLED(1, 0, 0, 0)
    if (n > 3):
        if (random.randint(0, 10) == 10):
            bird.setTriLED(1, 20, random.randint(0, 20), random.randint(0, 20))
        else:
            bird.setTriLED(1, 100, 0, 0)
    else:
        bird.setLED(n, 80)


async def scanner(bird):
    while True:
        for i in range(1, 5):
            scanner_delay = 0.01 if (bird.getLight(1) > 65) else 0.5
            scanner_leds(bird, i)
            await asyncio.sleep(scanner_delay)


async def spinner(bird):
    while True:
        bird.setPositionServo(1, random.uniform(0, 180))
        #bird.setPositionServo(1, 90)
        await asyncio.sleep(random.uniform(0, 0.25))


async def extra_rgb(bird):
    while True:
        bird.setTriLED(2, random.randint(0, 80), random.randint(0, 80), random.randint(0, 80))
        await asyncio.sleep(0.01)


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
