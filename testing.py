import pyttsx3
from pynput.keyboard import Key, Listener

engine = pyttsx3.init()

def on_press(key):
    print('{0} pressed'.format(key))
    engine.say('{0}'.format(key))
    engine.runAndWait()

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()