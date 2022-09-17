from enum import Enum
from time import sleep

class BotStates(Enum):
  INIT = 1
  START = 2
  GET_ALT_ORB_POSITION = 3
  GET_AUG_ORB_POSITION = 4
  GET_ITEM_POSITION = 5

class Bot:
  not_shutdown = True
  block_state_change = False
  state = BotStates.INIT

  def next_command(self):
    if self.block_state_change:
      print("block_state_change", self.state)
    if self.state == BotStates.INIT:
      print("press \"ctrl + alt + p\" to start", self.state)
    if self.state == BotStates.START:
      print("position the mouse on ALTERATION ORB: press ctrl+alt+o", self.state)
    if self.state == BotStates.GET_ALT_ORB_POSITION:
      print("position the mouse on AUGMENTATION ORB: press ctrl+alt+o", self.state)
    if self.state == BotStates.GET_AUG_ORB_POSITION:
      print("position the mouse on ITEM: press ctrl+alt+o", self.state)
    if self.state == BotStates.GET_ITEM_POSITION:
      print("press \"ctrl + alt + p\" to BEGIN THE WORK", self.state)
  
  def set_next_state(self):
    print(self.state)
    if self.block_state_change:
      return
    if self.state == BotStates.START:
      self.state = BotStates.GET_ALT_ORB_POSITION
    if self.state == BotStates.GET_ALT_ORB_POSITION:
      self.state = BotStates.GET_AUG_ORB_POSITION
    if self.state == BotStates.GET_AUG_ORB_POSITION:
      self.state = BotStates.GET_ITEM_POSITION
    self.block_state_change = True
    sleep(1)
    self.block_state_change = False
  
  def set_state_to_alt_orb_position(self):
    self.state = BotStates.GET_ALT_ORB_POSITION
  
  def set_state_to_aug_orb_position(self):
    self.state = BotStates.GET_AUG_ORB_POSITION
  
  def set_state_to_item_position(self):
    self.state = BotStates.GET_ITEM_POSITION
  
  def start_bot(self):
    if self.state == BotStates.INIT:
      self.state = BotStates.START
    self.block_state_change = True
    sleep(1)
    self.block_state_change = False