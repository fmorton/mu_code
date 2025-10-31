from library import *

bird = Hummingbird("A")

bird.stop_all()

for i in range(10):
    direction = random.randint(-100, 100)

    bird.tri_led(
        2, random.randint(50, 100), random.randint(0, 100), random.randint(0, 100)
    )
    bird.rotation_servo(1, direction)

    sleep(random.uniform(0.25, 1.5))

bird.stop_all()
