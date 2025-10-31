from library import *

bird = Hummingbird("A")

bird.stop_all()
sleep(3)

bird.rotation_servo(1, 90)
bird.rotation_servo(2, -100)
sleep(90)

# bird.rotation_servo(1, -50)
# sleep(5)

bird.stop_all()
