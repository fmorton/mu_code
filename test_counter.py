from robot.hummingbird import Hummingbird


counter = 0

while True:
    counter = counter + 1

    if counter > 100000000:
        print("GO")
        counter = 0
