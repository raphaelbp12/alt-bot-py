from pynput import keyboard
import threading

from bot import Bot

bot = Bot()
def botThread():
    while bot.not_shutdown:
        bot.next_command()
def on_press(key):
    bot.receive_key_press(key)
    # print('\n', "on_press", '{0}'.format(key), '\n')

def on_release(key):
    bot.receive_key_release(key)
    if key == keyboard.Key.end:
        bot.not_shutdown = False
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    thread = threading.Thread(target = botThread)
    thread.start()
    listener.join()