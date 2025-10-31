from birdbrain import Hummingbird
from time import sleep

bird = Hummingbird("A")

bird.led(1, 100)
sleep(1)

bird.stop_all()
