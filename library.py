import sys

from BirdBrain import Hummingbird
from time import sleep


class Library:
    def reset(bird):
        bird.setLED(1, 0)
        bird.setLED(2, 0)
        bird.setLED(3, 0)
