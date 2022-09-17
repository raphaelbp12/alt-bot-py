from pynput import keyboard

class Flags:
  is_ctrl_pressed = False
  is_alt_pressed = False

  def check_received_ctrl_press(self, key):
    if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r or key == keyboard.Key.ctrl:
      self.is_ctrl_pressed = True

  def check_received_ctrl_release(self, key):
    if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r or key == keyboard.Key.ctrl:
      self.is_ctrl_pressed = False

  def check_received_alt_press(self, key):
    if key == keyboard.Key.alt_l or key == keyboard.Key.alt_r or key == keyboard.Key.alt:
      self.is_alt_pressed = True

  def check_received_alt_release(self, key):
    if key == keyboard.Key.alt_l or key == keyboard.Key.alt_r or key == keyboard.Key.alt:
      self.is_alt_pressed = False