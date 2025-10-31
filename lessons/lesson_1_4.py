from birdbrain import Hummingbird
from time import sleep


def turn_all_on(bird, intensity):
    bird.led(1, intensity)
    bird.led(2, intensity)
    bird.led(3, intensity)
    sleep(2)


bird = Hummingbird("A")

for intensity in [100, 75, 50, 25]:
    turn_all_on(bird, intensity)

bird.stop_all()
