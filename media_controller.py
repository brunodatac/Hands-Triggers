import pygame
import pyautogui

pygame.init()
pygame.mixer.init()

while True:
    text = input("Digite o texto: ")  # recebe um texto do usuário
    if "play" == text.lower():  # verifica se a string "play" está presente no texto
        pyautogui.press('playpause')  # pressiona a tecla de mídia play/pause usando a biblioteca PyAutoGUI
        print("Tecla de mídia play/pause pressionada.")
    if "p" == text.lower():
        pyautogui.press('nexttrack')
        print("Proximo")
    if "v" == text.lower():
        pyautogui.press('prevtrack')   
        print("Voltar")