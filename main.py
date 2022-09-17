from pynput import keyboard
import threading

from bot import Bot

bot = Bot()
stop_bot = False
def botThread():
    global stop_bot
    while not bot.shutdown:
        if stop_bot:
            break
        bot.next_command()
def on_press(key):
    bot.receive_key_press(key)
    # print('\n', "on_press", '{0}'.format(key), '\n')

def on_release(key):
    global stop_bot
    if key == keyboard.Key.end:
        bot.shutdown = True
        stop_bot = True
        # Stop listener
        return False
    bot.receive_key_release(key)

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    thread = threading.Thread(target = botThread)
    thread.start()
    listener.join()