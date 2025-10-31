from time import sleep

from birdbrain import Hummingbird

bird = Hummingbird()

bird.rotation_servo(1, 9)
sleep(1)

bird.rotation_servo(1, 0)
sleep(1)

bird.rotation_servo(1, 9)
sleep(1)

bird.stop_all()
