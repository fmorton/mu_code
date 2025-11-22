import random

from robot.hummingbird import Hummingbird
from time import sleep

SERVO_SIDE_TO_SIDE = 1
SERVO_UP_DOWN = 2

hummingbird = Hummingbird("A")

while True:
    hummingbird.position_servo(SERVO_SIDE_TO_SIDE, random.randint(60, 85))
    hummingbird.position_servo(SERVO_UP_DOWN, random.randint(60, 100))

    sleep(random.uniform(0.3, 0.8))
