from library import *

bird = Hummingbird("A")

bird.stopAll()
sleep(3)

bird.tri_led(1, 20, 20, 20)
sleep(1)
bird.tri_led(1, 80, 80, 80)
