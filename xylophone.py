from library import *

TRAVEL_TIME = 0.25
WHOLE_NOTE_DELAY = 0.5


def reset():
    bird.position_servo(2, 120)
    bird.position_servo(1, 75)


def play_note():
    bird.position_servo(2, 96)
    sleep(0.12)

    bird.position_servo(2, 120)


def note_angle(note):
    if note == "C":
        return 170  # lower C
    if note == "D":
        return 145
    if note == "E":
        return 115
    if note == "F":
        return 85
    if note == "G":
        return 55
    if note == "A":
        return 35
    if note == "B":
        return 15
    if note == "2":
        return 2

    return 90


def rhythym_delay(delay):
    if delay == " ":
        return WHOLE_NOTE_DELAY
    if delay == "Q":
        return WHOLE_NOTE_DELAY / 4
    if delay == "H":
        return WHOLE_NOTE_DELAY / 2
    if delay == "W":
        return WHOLE_NOTE_DELAY
    if delay == "E":
        return WHOLE_NOTE_DELAY / 8

    return WHOLE_NOTE_DELAY


def play(note, delay):
    print(offset, note, delay, note_angle(note), rhythym_delay(delay))

    if note != "-":
        bird.position_servo(1, note_angle(note))
        sleep(TRAVEL_TIME)

        play_note()

    sleep(rhythym_delay(delay))


bird = Hummingbird("A")

song = "CCDCFECCDCGFCCBAFEDBBAFGF"
rhythym = "E    WE    WE     WE     "

reset()

for offset in range(len(song)):
    note = song[offset]
    delay = rhythym[offset]

    play(song[offset], rhythym[offset])

reset()
