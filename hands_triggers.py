import os
import subprocess
import threading
import time

from ultralytics import YOLO
import torch
import cv2

from voice_search import Voice

model = YOLO(r"D:\Projetos\Hand-Signals\train\best_low_res.pt")


cap = cv2.VideoCapture(0)


cont = 0


while True:
    
    # Lendo cada frame do vídeo
    ret, img = cap.read()
    if not ret:
        break
        
    # Executando a predição com o modelo YOLO
    time.sleep(0.5)
    results_v = model.predict(img,  conf=0.65, classes=21, show=False)
    results_l = model.predict(img,  conf=0.65, classes=11, show=False)
        
    for result in results_v:
        #box.append(result.boxes.cls)
        for tensor in result.boxes.cls:
            if torch.allclose(tensor, torch.tensor([21.])):
                cont += 1
                if cont == 1:
                    processo = Voice()
                    processo.abrir()
                    pass
    

    for result_l in results_l:
        #box.append(result.boxes.cls)
        for tensor_l in result_l.boxes.cls:
            if torch.allclose(tensor_l, torch.tensor([11.])):
                if cont >= 1:
                    processo.fechar('y')
                    #processo.terminate()
                    cont = 0
                    pass
