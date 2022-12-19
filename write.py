from pynput.keyboard import Listener, Key
from datetime import datetime

keys = []
timer = datetime.now()
file = open("code.txt", 'w', encoding='utf-8')

def reset_timer():
    global timer
    now = datetime.now()
    ts = now.timestamp() - timer.timestamp()
    timer = now
    file.write(f"sleep({ts})\n")

def on_press(key):
    if key in keys: return True
    keys.append(key)
    reset_timer()
    if type(key) is Key:
        file.write(f"keyboard.press(Key.{key.name})\n")
    else:
        file.write(f"keyboard.press(KeyCode({key.vk}))\n")

def on_release(key):
    if key in keys: keys.remove(key)
    reset_timer()
    if type(key) is Key:
        file.write(f"keyboard.release(Key.{key.name})\n")
    else:
        file.write(f"keyboard.release(KeyCode({key.vk}))\n")
    if key == Key.esc:
        file.close()
        return False

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()