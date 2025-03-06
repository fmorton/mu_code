from time import sleep
import random

from birdbrain_hummingbird import BirdbrainHummingbird

bird = BirdbrainHummingbird("A")

while True:
    light_level = bird.getLight(1) + 35
    print("Hello",light_level)

    #bird.play_note(light_level, 0.1)
    a = [0 for i in range(25)]
    #a = [random.randint(0, 1) for i in range(25)]
    bird.display(a)
