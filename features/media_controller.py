import pyautogui
import torch
import time

from .popup import Display

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

    def media_control(self, n_classe):        
        if torch.allclose(n_classe, torch.tensor([1.])): # classe: B | play/pause
            Display.processbar("PLAY/PAUSE", 0.15)
            self.playpause()

        elif torch.allclose(n_classe, torch.tensor([24.])): # classe: Y | proxima faixa
            Display.processbar("NEXT", 0.15)
            self.nexttrack()
        
        elif torch.allclose(n_classe, torch.tensor([11.])): # classe: L | voltar faixa
            Display.processbar("BACK", 0.15)
            self.prevtrack()

