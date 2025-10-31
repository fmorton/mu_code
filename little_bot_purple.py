import random
import time

from birdbrain_python_library_2.birdbrain_hummingbird import BirdbrainHummingbird

SERVO_SIDE_TO_SIDE = 1
SERVO_UP_DOWN = 2

hummingbird = BirdbrainHummingbird('A')

while True:
    hummingbird.position_servo(SERVO_SIDE_TO_SIDE, random.randint(60, 110))
    hummingbird.position_servo(SERVO_UP_DOWN, random.randint(90, 90))
    time.sleep(random.uniform(0.2, 0.6))
