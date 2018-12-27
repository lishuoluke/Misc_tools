# This script simulate the Ctrl + C from keyboard

from pynput.keyboard import Key, Controller

keyboard = Controller()


keyboard.press(Key.ctrl)
keyboard.press('c')
keyboard.release('c')
keyboard.release(Key.ctrl)
