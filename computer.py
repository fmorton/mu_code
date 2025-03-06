from time import sleep
import random

from BirdBrain import Hummingbird
from birdbrain_hummingbird import BirdbrainHummingbird

bird = BirdbrainHummingbird("A")

for i in range(200):
    a = [random.randint(0, 1) for i in range(25)]
    bird.display(a)

    bird.play_note(random.randint(32, 120), 0.025)
    sleep(random.uniform(0, 0.1))

bird.stopAll()
