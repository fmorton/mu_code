import random

from birdbrain import Hummingbird
from time import sleep

SERVO_SIDE_TO_SIDE = 1
SERVO_UP_DOWN = 2

hummingbird = Hummingbird("A")

while True:
    hummingbird.position_servo(SERVO_SIDE_TO_SIDE, random.randint(60, 110))
    hummingbird.position_servo(SERVO_UP_DOWN, random.randint(90, 90))

    sleep(random.uniform(0.2, 0.6))
