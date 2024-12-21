import sys
import asyncio
import datetime
import random

from BirdBrain import Hummingbird
from time import sleep


class Library:
    def reset_hummingbird(bird, sleep_amount):
        bird.setLED(1, 0)
        bird.setLED(2, 0)
        bird.setLED(3, 0)
        bird.setTriLED(1, 0, 0, 0)
        bird.setTriLED(2, 0, 0, 0)
        bird.setRotationServo(1, 0)
        bird.setRotationServo(2, 0)
        bird.setRotationServo(3, 0)
        bird.setRotationServo(4, 0)
        sleep(sleep_amount)
