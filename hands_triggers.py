import os
import subprocess
import threading
import time

from ultralytics import YOLO
import torch
import cv2


model = YOLO(r"D:\Projetos\Hand-Signals\train\best_low_res.pt")

control_file = 'D:\projetos\Hand-Signals\stop_voice_search.txt'

cap = cv2.VideoCapture(0)


cont = 0

while True:
    
    # Lendo cada frame do vídeo
    ret, img = cap.read()
    if not ret:
        break

    with torch.no_grad():
        # Executando a predição com o modelo YOLO
        results_v = model.predict(img,  conf=0.65, classes=21, show=False)
        results_l = model.predict(img,  conf=0.65, classes=11, show=False)
        
    for result in results_v:
        #box.append(result.boxes.cls)
        for tensor in result.boxes.cls:
            if torch.allclose(tensor, torch.tensor([21.])):
                cont += 1
                if cont == 1:
                    if os.path.exists(control_file):
                        # Remove o arquivo de controle e encerra a execução do script
                        os.remove(control_file)
                        
                    processo = subprocess.Popen(['python', 'voice_search.py'])
                    pass
    

    for result_l in results_l:
        #box.append(result.boxes.cls)
        for tensor_l in result_l.boxes.cls:
            if torch.allclose(tensor_l, torch.tensor([11.])):
                with open("stop_voice_search.txt", "w") as f:
                    f.write("Encerrar script")
                processo.terminate()
                cont = 0
                break
            

cap.release()
cv2.destroyAllWindows()
