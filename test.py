from library import *

import random

while True:
    print(random.randint(1, 2))

bird = Hummingbird("A")

bird.stop_all()
sleep(3)

bird.tri_led(1, 20, 20, 20)
sleep(1)
bird.tri_led(1, 80, 80, 80)
