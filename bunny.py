import random

from birdbrain import Hummingbird
from time import sleep

LIGHT_CUTOFF_LEVEL = 7


def random_event():
    return random.random() < 0.05


def r(maximum):
    return random.randint(0, maximum)


def light_sensor_not_covered():
    bird.position_servo(1, 90)
    bird.position_servo(2, 90)

    if random_event():
        bird.position_servo(1, 100)

    bird.led(1, 2)
    bird.led(2, 4)

    bird.tri_led(1, r(3), r(3), r(7))


def light_sensor_covered():
    bird.position_servo(1, 120)
    bird.position_servo(2, 60)

    bird.led(1, 80)
    bird.led(2, 80)

    bird.tri_led(1, r(100), r(100), r(100))

    sleep(0.10)

    bird.position_servo(1, 90)
    bird.position_servo(2, 90)

    bird.tri_led(1, r(100), r(100), r(100))

    sleep(0.10)


bird = Hummingbird("A")

while True:
    if bird.light(1) < LIGHT_CUTOFF_LEVEL:
        light_sensor_covered()
    else:
        light_sensor_not_covered()
