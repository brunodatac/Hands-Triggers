import os
import subprocess
import threading
import time

from ultralytics import YOLO
import torch
import cv2

from voice_search import Voice
from media_controller import Controller


def search(n_classe):
    global processo, pesquisa_executando

    if torch.allclose(n_classe, torch.tensor([21.])): # classe: V | pesquisa de voz
        if not pesquisa_executando:
            pesquisa_executando = True
            processo = Voice()
            processo.abrir()

    elif torch.allclose(n_classe, torch.tensor([11.])): # classe: L | fechar pesquisa de voz
        if pesquisa_executando:
            pesquisa_executando = False
            processo.fechar('y')
    else:
        return "Invalid case"



model = YOLO(r"D:\Projetos\Hand-Signals\train\best_low_res.pt")
cap = cv2.VideoCapture(0)
pesquisa_executando = False
processo = None

while True:
    
    # Lendo cada frame do vídeo
    ret, img = cap.read()
    if not ret:
        break
        
    # Executando a predição com o modelo YOLO
    time.sleep(0.5)
    results = model.predict(img,  conf=0.80, show=False)
        
    for result in results:
        #box.append(result.boxes.cls)
        for tensor in result.boxes.cls:
            search(tensor)

