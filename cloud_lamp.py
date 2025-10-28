from time import sleep
import random

from birdbrain_python_library_2.birdbrain_hummingbird import BirdbrainHummingbird

def off(bird):
    bird.tri_led(1, 0, 0, 0)
    bird.tri_led(2, 0, 0, 0)

def on(bird, port, brightness):
    bird.tri_led(port, brightness, brightness, brightness)

bird = BirdbrainHummingbird('A')

off(bird)

brightness_list = [ 0, 0, 0, 0, 0, 20, 40, 60, 80, 100 ]

while True:
    on(bird, 1, random.choice(brightness_list))
    on(bird, 2, random.choice(brightness_list))

    sleep(random.uniform(0.05, 0.3333))

    off(bird)

    sleep(random.uniform(0.1, 0.75))
