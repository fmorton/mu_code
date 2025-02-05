from BirdBrain import Hummingbird
from time import sleep

def turn_all_on(bird, intensity):
    bird.setLED(1, intensity)
    bird.setLED(2, intensity)
    bird.setLED(3, intensity)
    sleep(2)

bird = Hummingbird('A')

for intensity in [ 100, 75, 50, 25 ]: turn_all_on(bird, intensity)

bird.stopAll()
