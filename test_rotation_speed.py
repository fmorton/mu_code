from time import sleep

from BirdBrain import Hummingbird

bird = Hummingbird()

bird.setRotationServo(1, 9)
sleep(1)

bird.setRotationServo(1, 0)
sleep(1)

bird.rotation_servo(1, 9)
sleep(1)

bird.stop_all()
