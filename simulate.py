from time import sleep
from pynput.keyboard import Controller, KeyCode, Key

with open ("code.txt", "r") as file:
    data = file.read()

keyboard = Controller()

sleep(5)
exec(data)