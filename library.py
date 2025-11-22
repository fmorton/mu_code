import sys
import asyncio
import datetime
import random

from robot.hummingbird import Hummingbird
from tasks import Tasks
from time import sleep


class Library:
    def reset_hummingbird(bird, sleep_amount):
        bird.led(1, 0)
        bird.led(2, 0)
        bird.led(3, 0)
        bird.tri_led(1, 0, 0, 0)
        bird.tri_led(2, 0, 0, 0)
        bird.rotation_servo(1, 0)
        bird.rotation_servo(2, 0)
        bird.rotation_servo(3, 0)
        bird.rotation_servo(4, 0)
        sleep(sleep_amount)
