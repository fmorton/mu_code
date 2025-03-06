from time import sleep
import random

from birdbrain_hummingbird import BirdbrainHummingbird

bird = BirdbrainHummingbird('A')

bird.led(2, 100)

while True:
    bird.led(random.randint(1, 2), 100)
    sleep(random.uniform(0.1, 2.0))
    bird.led(1, 0)
    bird.led(2, 0)
    sleep(0.1)


