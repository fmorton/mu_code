from time import sleep

from BirdBrain import Hummingbird

def play(bird, note, beats = 1):
    bird.playNote(note, beats)
    sleep(beats)


bird = Hummingbird()

play(bird, 50)
play(bird, 60, 2)
