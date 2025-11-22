import random

from robot.hummingbird import Hummingbird
from time import sleep

bird = Hummingbird("A")

for i in range(200):
    a = [random.randint(0, 1) for i in range(25)]
    bird.display(a)

    bird.play_note(random.randint(32, 120), 0.025)
    sleep(random.uniform(0.0, 0.1))

bird.stop_all()
