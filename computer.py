from BirdBrain import Hummingbird
from time import sleep
import random

bird = Hummingbird("A")

for i in range(200):
    a = [random.randint(0, 1) for i in range(25)]
    bird.setDisplay(a)

    bird.playNote(random.randint(32, 120), 0.025)
    sleep(random.uniform(0, 0.1))

bird.stopAll()
