from library import *

bird = Hummingbird('A')

bird.stopAll()
sleep(3)

bird.setRotationServo(1, 100)
sleep(90)

#bird.setRotationServo(1, -50)
#sleep(5)

bird.stopAll()
