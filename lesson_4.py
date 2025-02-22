from library import *
from time import sleep

bird = Hummingbird('A')

bird.setPositionServo(1, 90)
sleep(0.5)
bird.setPositionServo(1, 0)
sleep(0.5)

for i in range(180):
    bird.setPositionServo(1, i)
    #sleep(0.05)

for i in reversed(range(180)):
    bird.setPositionServo(1, i)
    #sleep(0.05)
