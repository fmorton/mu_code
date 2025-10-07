from BirdBrain import Hummingbird
from time import sleep
import random

TARGET_SERVO = 1
TARGET_HOME = 36
TARGET_DOWN = 120

MOVE_SERVO = 2
MOVE_HOME = 165
MOVE_LEFT = 178
MOVE_RIGHT = 130

HOME_NOT_HIT = 45
HOME_HIT = 140

bird = Hummingbird("A")

bird.position_servo(TARGET_SERVO, TARGET_HOME)
bird.position_servo(MOVE_SERVO, MOVE_HOME)

move_count = 0
move_target = random.randint(50, 150)

while True:
    bird.position_servo(TARGET_SERVO, TARGET_HOME)
    move_target = random.randint(20, 40)

    if(bird.light(1) < 92):
        move_count += 1
        if move_count > move_target:
            move_count = 0
            move_target = random.randint(MOVE_RIGHT, MOVE_LEFT)

            bird.position_servo(MOVE_SERVO, move_target)
    else:
        bird.position_servo(TARGET_SERVO, TARGET_DOWN)
        bird.position_servo(MOVE_SERVO, MOVE_HOME)

        sleep(2)

        bird.position_servo(TARGET_SERVO, TARGET_HOME)
