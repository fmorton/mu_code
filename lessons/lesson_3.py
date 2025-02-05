from BirdBrain import Hummingbird
from time import sleep
import random

bird = Hummingbird("A")

bird.print("Hi")
sleep(1)

for i in range(0):
    bird.setDisplay(
        [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    )
    sleep(0.5)
    bird.setDisplay(
        [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    )
    sleep(0.5)

for i in range(200):
    a = [random.randint(0, 1) for i in range(25)]
    bird.setDisplay(a)
    bird.playNote(random.randint(80, 110), 0.025)
    sleep(0.1)

bird.stopAll()
