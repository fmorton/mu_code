import time

from birdbrain import Hummingbird
from time import sleep

MULTIPLIER = 1.0

bird = Hummingbird("A")
bird.stop_all()

for i in range(10):
    balanced = bird.magnetometer()[0]
    print("balancing", balanced)
    sleep(0.5)

print("DEBUG: balanced is", balanced)


def forward(bird, orientation):
    # print("forward", orientation)
    bird.rotation_servo(1, -11 * MULTIPLIER)
    bird.rotation_servo(2, 25 * MULTIPLIER)
    # sleep(0.1)
    # stop(bird)


def backward(bird, orientation):
    # print("backward", orientation)
    bird.rotation_servo(1, 10 * MULTIPLIER)
    bird.rotation_servo(2, -11 * MULTIPLIER)
    # sleep(0.1)
    # stop(bird)


def stop(bird):
    # print("stop")
    bird.rotation_servo(1, 0)
    bird.rotation_servo(2, 0)


orientation = balanced

while True:
    if orientation > balanced:
        forward(bird, orientation)
    elif orientation < balanced:
        backward(bird, orientation)
    else:
        stop(bird)

    start_time = time.perf_counter()
    orientation = bird.magnetometer()[0]
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"The command took {elapsed_time:.4f} seconds to execute.")
