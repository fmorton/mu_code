from robot.hummingbird import Hummingbird
from time import sleep


def play(bird, note, beats=1):
    bird.play_note(note, beats)
    sleep(beats)


bird = Hummingbird()

play(bird, 50)
play(bird, 60, 2)
