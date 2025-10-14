from BirdBrain import Hummingbird
from time import sleep

bird = Hummingbird("A")

bird.setLED(1, 100)
sleep(1)

bird.stopAll()
