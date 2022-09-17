from time import sleep
import numpy as np
import threading
from pynput.mouse import Button, Controller
from pynput import keyboard

from bot import Bot

class MyException(Exception): pass

listener = None
bot = Bot()
def main():

    # def botThread():
    #     while bot.not_shutdown:
    #         bot.next_command()

    def start_bot():
        print(bot.state)
        bot.start_bot()

    def set_next_state():
        print(bot.state)
        bot.set_next_state()

    HOTKEYS = [
        keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+<alt>+p'), start_bot),
        keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+<alt>+o'), set_next_state)
    ]

    def on_press(key):
        for hotkey in HOTKEYS:
            hotkey.press(listener.canonical(key))
        if key == keyboard.Key.esc:
            bot.not_shutdown = False
            raise MyException(key)

    def on_release(key):
        for hotkey in HOTKEYS:
            hotkey.release(listener.canonical(key))
        if key == keyboard.Key.esc:
            bot.not_shutdown = False
            return False

    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as l:
        listener = l
        # thread = threading.Thread(target = botThread)
        # thread.start()
        l.join()

main()