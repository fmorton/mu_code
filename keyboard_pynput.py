from pynput import keyboard
import time

def on_press(key):
    try:
        print(f"Key pressed: {key.char}")
    except AttributeError:
        print(f"Special key pressed: {key}")

listener = keyboard.Listener(on_press=on_press)
listener.start()

while True:
    # Do other work
    print("Program running...")
    time.sleep(1)
