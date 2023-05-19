from ultralytics import YOLO
import torch
import time
import sys
import cv2

import features



model = YOLO(r"D:\Projetos\Hand-Signals\train\best_newds.pt")

cap = cv2.VideoCapture(0)
voice = features.Voice()
controller = features.Controller()
pesquisa_executando = False
processo = None
loop = True

features.Display.processbar("Iniciando...", 0.65)



while loop:

    # Lendo cada frame do vídeo
    ret, img = cap.read()
    if not ret:
        break

    # Executando a predição com o modelo YOLO
    time.sleep(0.5)
    results = model.predict(img,  conf=0.80, stream=True, show=False)

    for result in results:
        #box.append(result.boxes.cls)
        for tensor in result.boxes.cls:
            voice.search(tensor)
            controller.media_control(tensor)
            
            if torch.allclose(tensor, torch.tensor([2.])): # classe: C | Encerra o script
                loop = False


features.Display.processbar("Encerrando...", 1)
sys.exit("-"*98 + "\n")