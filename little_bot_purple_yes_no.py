import random

from birdbrain import Hummingbird
from time import sleep

SERVO_UP_DOWN = 1
SERVO_SIDE_TO_SIDE = 2

hummingbird = Hummingbird("A")

while True:
    if hummingbird.light(1) < 10:
        print("LOOK")
        hummingbird.position_servo(SERVO_UP_DOWN, 60)
        hummingbird.position_servo(SERVO_SIDE_TO_SIDE, 70)

        while hummingbird.light(1) < 10:
            sleep(0.25)
        print("ANSWER")

    print("LOOK AROUND")
    hummingbird.position_servo(SERVO_UP_DOWN, random.randint(60, 100))
    hummingbird.position_servo(SERVO_SIDE_TO_SIDE, random.randint(50, 95))

    sleep(random.uniform(0.4, 0.8))
