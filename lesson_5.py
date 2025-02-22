from library import *

bird = Hummingbird("A")

bird.stopAll()

for i in range(10):
    direction = random.randint(-100, 100)

    bird.setTriLED(2, random.randint(50, 100), random.randint(0, 100), random.randint(0, 100))
    bird.setRotationServo(1, direction)

    sleep(random.uniform(0.25, 1.5))

bird.stopAll()
