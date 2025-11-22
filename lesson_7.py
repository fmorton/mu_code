from time import sleep
import random

from robot.hummingbird import Hummingbird

bird = Hummingbird("A")

while True:
    light_level = bird.light(1) + 35
    print("Hello", light_level)

    # bird.play_note(light_level, 0.1)
    a = [0 for i in range(25)]
    # a = [random.randint(0, 1) for i in range(25)]
    bird.display(a)
