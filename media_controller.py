import pyautogui
import time

class Controller():
    
    def playpause(self):
        pyautogui.press('playpause')  # biblioteca PyAutoGUI
        time.sleep(1.5)

    def nexttrack(self):
        pyautogui.press('nexttrack')
        time.sleep(1.5)

    def prevtrack(self):
        pyautogui.press('prevtrack')
        pyautogui.press('prevtrack')
        time.sleep(1.5)
