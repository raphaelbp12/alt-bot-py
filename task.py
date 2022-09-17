from pynput.mouse import Button
from pynput.keyboard import Key, Controller
from enum import Enum
from time import sleep
import win32clipboard

class WorkingStates(Enum):
    INIT = 1
    USE_ALT = 2
    USE_AUG = 3
    FINISHED = 4
    PAUSED = 5

class Task:
    keyboard = Controller()
    state = WorkingStates.INIT

    mods = ["Sprinter's"]

    def tick(self, mouse, alt_pos, aug_pos, item_pos):
        if self.state == WorkingStates.INIT:
            self.state = WorkingStates.USE_ALT
        elif self.state == WorkingStates.USE_ALT:
            self.use_alt(mouse, alt_pos, item_pos)
            sleep(0.1)
        elif self.state == WorkingStates.USE_AUG:
            self.use_aug(mouse, aug_pos, item_pos)
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
        self.random_sleep()
        self.keyboard.press(Key.ctrl_l)
        self.keyboard.press('c')
        self.keyboard.release('c')
        self.keyboard.release(Key.ctrl_l)
        self.random_sleep()

        win32clipboard.OpenClipboard()
        data: str = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        self.random_sleep()

        data_exploded = data.split("--------")
        names_raw = data_exploded[0]
        names_exploded = names_raw.splitlines()
        item_name = names_exploded[-1]

        mods_found_num = 0
        for mod in self.mods:
            if mod in item_name:
                mods_found_num += 1
        
        return mods_found_num > 0

    def use_alt(self, mouse, alt_pos, item_pos):
        mouse.position = alt_pos
        self.random_sleep()
        self.press_mouse_right(mouse)
        self.random_sleep()
        mouse.position = item_pos
        self.random_sleep()
        self.press_mouse_left(mouse)
        self.random_sleep()
        # check item
        if self.check_item():
            self.state = WorkingStates.FINISHED
            return
        self.state = WorkingStates.USE_AUG

    def use_aug(self, mouse, aug_pos, item_pos):
        mouse.position = aug_pos
        self.random_sleep()
        self.press_mouse_right(mouse)
        self.random_sleep()
        mouse.position = item_pos
        self.random_sleep()
        self.press_mouse_left(mouse)
        self.random_sleep()
        # check item
        if self.check_item():
            self.state = WorkingStates.FINISHED
            return
        self.state = WorkingStates.USE_ALT