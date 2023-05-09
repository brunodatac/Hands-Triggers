import os
import subprocess
import threading
import time

from ultralytics import YOLO
import torch
import cv2

from voice_search import Voice


def v_signal():
    global cont, processo
    cont += 1
    if cont == 1:
        processo = Voice()
        processo.abrir()



def l_signal():
    global cont, processo
    if cont >= 1:
        processo.fechar('y')
        cont = 0



def switch_case(n_classe):
    switcher = {
        torch.tensor([21.]): v_signal(),
        torch.tensor([11.]): l_signal()
    }
    return switcher.get(n_classe, "Invalid classe")



model = YOLO(r"D:\Projetos\Hand-Signals\train\best_low_res.pt")
cap = cv2.VideoCapture(0)
cont = 0
processo = None

while True:
    
    # Lendo cada frame do vídeo
    ret, img = cap.read()
    if not ret:
        break
        
    # Executando a predição com o modelo YOLO
    time.sleep(0.5)
    results = model.predict(img,  conf=0.65, show=False)
        
    for result in results:
        #box.append(result.boxes.cls)
        for tensor in result.boxes.cls:
            switch_case(tensor)

