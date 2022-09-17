from enum import Enum
from sys import flags
from time import sleep

from flags import Flags

class BotStates(Enum):
  INIT = 1
  START = 2
  GET_ALT_ORB_POSITION = 3
  GET_AUG_ORB_POSITION = 4
  GET_ITEM_POSITION = 5

class Bot:
  flags = Flags()
  not_shutdown = True
  block_state_change = False
  state = BotStates.INIT

  def next_command(self):
    if self.block_state_change:
      return
    if self.state == BotStates.INIT:
      print("press \"ctrl + alt + p\" to start", end="\r")
    if self.state == BotStates.START:
      print("position the mouse on ALTERATION ORB: press ctrl+alt+o", end="\r")
    if self.state == BotStates.GET_ALT_ORB_POSITION:
      print("position the mouse on AUGMENTATION ORB: press ctrl+alt+o", end="\r")
    if self.state == BotStates.GET_AUG_ORB_POSITION:
      print("position the mouse on ITEM: press ctrl+alt+o", end="\r")
    if self.state == BotStates.GET_ITEM_POSITION:
      print("press \"ctrl + alt + p\" to BEGIN THE WORK", end="\r")
  
  def set_next_state(self):
    # print(self.state)
    if self.block_state_change:
      return
    if self.state == BotStates.START:
      self.set_state_to_alt_orb_position()
    elif self.state == BotStates.GET_ALT_ORB_POSITION:
      self.set_state_to_aug_orb_position()
    elif self.state == BotStates.GET_AUG_ORB_POSITION:
      self.set_state_to_item_position()
  
  def set_state_to_alt_orb_position(self):
    self.state = BotStates.GET_ALT_ORB_POSITION
  
  def set_state_to_aug_orb_position(self):
    self.state = BotStates.GET_AUG_ORB_POSITION
  
  def set_state_to_item_position(self):
    self.state = BotStates.GET_ITEM_POSITION
  
  def start_bot(self):
    if self.block_state_change:
      return
    if self.state == BotStates.INIT:
      self.state = BotStates.START

  def receive_key_press(self, key):
    self.flags.check_received_ctrl_press(key)
    self.flags.check_received_alt_press(key)
    if '{0}'.format(key) == "<79>":
        self.set_next_state()
        self.block_state_change = True
        # print("cctrl-alt-o", '\n')
    if '{0}'.format(key) == "<80>":
        self.start_bot()
        self.block_state_change = True
        # print("cctrl-alt-p", '\n')

  def receive_key_release(self, key):
    self.flags.check_received_ctrl_release(key)
    self.flags.check_received_alt_release(key)
    if not self.flags.is_alt_pressed and not self.flags.is_ctrl_pressed:
      self.block_state_change = False