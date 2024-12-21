from library import *


def set_random_tri_color(bird, port):
    red = random.randint(25, 80)
    green = random.randint(25, 80)
    blue = random.randint(25, 80)

    bird.setTriLED(port, red, green, blue)


def set_disco_ball(bird, angle):
    bird.setPositionServo(2, angle)
    set_random_tri_color(bird, 1)
    set_random_tri_color(bird, 2)


async def wheel(bird):
    while True:
        bird.setRotationServo(1, random.choice([10, -25, -30, -35, 0]))
        await asyncio.sleep(random.uniform(0, 5))


async def disco_ball(bird):
    while True:
        if bird.getDistance(1) < 14:
            bird.setLED(1, 50)

            for i in range(7):
                set_disco_ball(bird, 10)
                await asyncio.sleep(0.25)

                set_disco_ball(bird, 80)
                await asyncio.sleep(0.25)

        else:
            bird.setLED(1, 5)
            bird.setTriLED(1, 0, 0, 0)
            bird.setTriLED(2, 0, 0, 0)
            bird.setPositionServo(2, 45)

        await asyncio.sleep(0)


async def runner(bird):
    await asyncio.gather(wheel(bird), disco_ball(bird))


bird = Hummingbird("A")

Library.reset_hummingbird(bird, 2)

asyncio.run(runner(bird))
