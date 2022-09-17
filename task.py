from enum import Enum
from time import sleep

class WorkingStates(Enum):
    INIT = 1
    USE_ALT = 2
    USE_AUG = 3
    CHECK_ITEM = 4
    FINISHED = 5
    PAUSED = 6

class Task:
    state = WorkingStates.INIT

    def tick(self, mouse, alt_pos, aug_pos, item_pos):
        if self.state == WorkingStates.INIT:
            self.state = WorkingStates.USE_ALT
        elif self.state == WorkingStates.USE_ALT:
            mouse.position = alt_pos
            self.state = WorkingStates.USE_AUG
            sleep(0.5)
        elif self.state == WorkingStates.USE_AUG:
            mouse.position = aug_pos
            self.state = WorkingStates.CHECK_ITEM
            sleep(0.5)
        elif self.state == WorkingStates.CHECK_ITEM:
            mouse.position = item_pos
            self.state = WorkingStates.USE_ALT
            sleep(0.5)
