from birdbrain import Hummingbird
from time import sleep

bird = Hummingbird("A")  # Declare Hummingbird object

# Exercise 1 - changing the 100 to smaller numbers makes the LED less bright
bird.led(1, 100)  # Turn on LED 1
sleep(1)  # Wait 1 second

bird.led(1, 0)  # Turn on LED 1

# bird.stop_all()                  # Turn everything off

# Exercise 2
bird.led(1, 100)  # Turn on LED 1
sleep(5)  # Wait 5 seconds

# Exercise 3
bird.led(1, 100)  # Turn on LED 1
sleep(1)  # Wait 1 second
bird.led(1, 0)  # Turn off LED 1
bird.led(2, 100)  # Turn on LED 2
sleep(1)  # Wait 1 second

# Exercise 3 - modified
bird.led(1, 100)  # Turn on LED 1
sleep(1)  # Wait 1 second
bird.led(1, 0)  # Turn off LED 1
bird.led(2, 100)  # Turn on LED 2
sleep(1)  # Wait 1 second
bird.led(3, 100)  # Turn on LED 3
sleep(1)  # Wait 1 second

# Exercise 4
bird.led(1, 100)  # Turn on LED 1
bird.led(2, 100)  # Turn on LED 2
bird.led(3, 100)  # Turn on LED 3
sleep(2)
bird.led(1, 75)  # Turn on LED 1 at 75%
bird.led(2, 75)  # Turn on LED 2 at 75%
bird.led(3, 75)  # Turn on LED 3 at 75%
sleep(2)
bird.led(1, 50)  # Turn on LED 1 at 50%
bird.led(2, 50)  # Turn on LED 2 at 50%
bird.led(3, 50)  # Turn on LED 3 at 50%
sleep(2)
bird.led(1, 25)  # Turn on LED 1 at 25%
bird.led(2, 25)  # Turn on LED 2 at 25%
bird.led(3, 25)  # Turn on LED 3 at 25%
sleep(2)

bird.stop_all()  # Turn everything off
