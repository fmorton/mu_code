from library import *

bird = Hummingbird("A")

Library.reset(bird)

bird.setLED(1, 100)
sleep(1)

bird.stopAll()
