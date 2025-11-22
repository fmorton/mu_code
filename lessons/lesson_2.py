from robot.hummingbird import Hummingbird
from time import sleep

bird = Hummingbird("A")

bird.tri_led(1, 49, 9, 90)
sleep(1)

bird.tri_led(1, 100, 0, 100)
sleep(1)
bird.tri_led(1, 0, 100, 100)
sleep(1)
bird.tri_led(1, 100, 100, 0)
sleep(1)

for i in range(5):
    bird.tri_led(1, 0, 100, 0)
    sleep(0.1)
    bird.tri_led(1, 100, 0, 0)
    sleep(0.1)

for i in range(100):
    bird.tri_led(1, i, 0, 100 - i)
    sleep(0.1)

bird.stop_all()
