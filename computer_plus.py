from library import *


async def bitmap(hummingbird):
    while True:
        a = [random.randint(0, 1) for i in range(25)]
        hummingbird.display(a)

        hummingbird.play_note(random.randint(32, 120), 0.025)

        await Tasks.yield_task()


def scanner_leds(hummingbird, n):
    hummingbird.led(1, 0)
    hummingbird.led(2, 0)
    hummingbird.led(3, 0)
    hummingbird.tri_led(1, 0, 0, 0)
    if n > 3:
        if random.randint(0, 10) == 10:
            hummingbird.tri_led(1, 20, random.randint(0, 20), random.randint(0, 20))
        else:
            hummingbird.tri_led(1, 100, 0, 0)
    else:
        hummingbird.led(n, 80)


async def scanner(hummingbird):
    while True:
        for i in range(1, 5):
            scanner_delay = 0.01 if (hummingbird.light(1) > 65) else 0.5
            scanner_leds(hummingbird, i)

            await Tasks.yield_task(scanner_delay)


async def spinner(hummingbird):
    while True:
        hummingbird.position_servo(1, random.uniform(0, 180))

        await Tasks.yield_task(random.uniform(0, 0.25))


async def extra_rgb(hummingbird):
    while True:
        hummingbird.tri_led(
            2, random.randint(0, 80), random.randint(0, 80), random.randint(0, 80)
        )

        await Tasks.yield_task()


hummingbird = Hummingbird("A")

tasks = Tasks()

tasks.create_task(bitmap(hummingbird))
tasks.create_task(scanner(hummingbird))
tasks.create_task(spinner(hummingbird))
tasks.create_task(extra_rgb(hummingbird))

tasks.run()

bird.stop_all()
