from birdbrain_hummingbird import BirdbrainHummingbird

from time import sleep

bird = BirdbrainHummingbird("A")

bird.setLED(1, 100)
sleep(1)

bird.led(1, 0)
sleep(1)

bird.led(1, 100)
sleep(1)

bird.stop_all()
