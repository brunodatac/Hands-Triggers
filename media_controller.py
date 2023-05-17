import pyautogui
import torch
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

    def media_control(self, n_classe):
        
        if torch.allclose(n_classe, torch.tensor([14.])): # classe: O | play/pause
            self.playpause()

        elif torch.allclose(n_classe, torch.tensor([8.])): # classe: I | proxima faixa
            self.nexttrack()
        
        elif torch.allclose(n_classe, torch.tensor([22.])): # classe: W | voltar faixa
            self.prevtrack()