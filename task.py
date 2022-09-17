from pynput.mouse import Button
from pynput.keyboard import Key, Controller
from enum import Enum
from time import sleep
import win32clipboard

class WorkingStates(Enum):
    INIT = 1
    USE_ALT = 2
    USE_AUG = 3
    CHECK_ITEM = 4
    FINISHED = 5
    PAUSED = 6

class Task:
    keyboard = Controller()
    state = WorkingStates.INIT

    def tick(self, mouse, alt_pos, aug_pos, item_pos):
        if self.state == WorkingStates.INIT:
            self.state = WorkingStates.USE_ALT
        elif self.state == WorkingStates.USE_ALT:
            self.use_alt(mouse, alt_pos, item_pos)
            sleep(0.1)
        elif self.state == WorkingStates.USE_AUG:
            mouse.position = aug_pos
            self.state = WorkingStates.CHECK_ITEM
            sleep(0.1)
        elif self.state == WorkingStates.CHECK_ITEM:
            mouse.position = item_pos
            self.state = WorkingStates.USE_ALT
            sleep(0.1)

    def random_sleep(self):
        sleep(0.01)

    def press_mouse_left(self, mouse):
        mouse.press(Button.left)
        self.random_sleep()
        mouse.release(Button.left)

    def press_mouse_right(self, mouse):
        mouse.press(Button.right)
        self.random_sleep()
        mouse.release(Button.right)

    def check_item(self):
        self.keyboard.press(Key.ctrl_l)
        self.keyboard.press('c')
        self.keyboard.release('c')
        self.keyboard.release(Key.ctrl_l)

        win32clipboard.OpenClipboard()
        data: str = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()

        data_exploded = data.split("--------")
        mods_raw = data_exploded[-1]
        mods_exploded = mods_raw.splitlines()

        print("data_exploded", len(data_exploded), "mods", len(mods_exploded))

    def use_alt(self, mouse, alt_pos, item_pos):
        mouse.position = alt_pos
        self.random_sleep()
        # self.press_mouse_right()
        self.random_sleep()
        mouse.position = item_pos
        self.random_sleep()
        # self.press_mouse_left()
        self.random_sleep()
        # check item
        self.check_item()
        self.state = WorkingStates.USE_AUG