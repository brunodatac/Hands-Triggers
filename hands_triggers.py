import os
import subprocess
import threading
import time

from ultralytics import YOLO
import torch
import cv2


model = YOLO(r"D:\Projetos\Hand-Signals\train\best_low_res.pt")

cap = cv2.VideoCapture(0)


cont = 0
# thread_voice_search = None

# def executa_voice_search():
#     global processo  # adiciona essa linha para poder acessar o processo fora da função
#     os.chdir(os.path.dirname(__file__))
#     processo = subprocess.Popen(['python', 'voice_search.py'], stdin=subprocess.PIPE)


while True:
    
    # Lendo cada frame do vídeo
    ret, img = cap.read()
    if not ret:
        break

    with torch.no_grad():
        # Executando a predição com o modelo YOLO
        results_v = model.predict(img,  conf=0.65, classes=21, show=False)
        results_w = model.predict(img,  conf=0.65, classes=22, show=False)
        
    for result in results_v:
        #box.append(result.boxes.cls)
        for tensor in result.boxes.cls:
            if torch.allclose(tensor, torch.tensor([21.])):
                cont += 1
                if cont == 1:
                    processo = subprocess.Popen(['python', 'voice_search.py'])
                    pass
                    processo.wait()
                    cont = 0
                    # processo.wait()
    
    # pra realizar o processo de multiplos scritps ao mesmo tempo
    # for result in results_v:
    #     #box.append(result.boxes.cls)
    #     for tensor in result.boxes.cls:
    #         if torch.allclose(tensor, torch.tensor([21.])):
    #             cont += 1
    #             if cont == 1:
    #                 thread_voice_search = threading.Thread(target=executa_voice_search)
    #                 thread_voice_search.start()

    for result_w in results_w:
        #box.append(result.boxes.cls)
        for tensor_w in result_w.boxes.cls:
            if torch.allclose(tensor_w, torch.tensor([22.])):
                processo.terminate() # fecha o programa
                cont = 0
                break
            
    # # Aguardando a tecla 'q' para finalizar a execução
    # if cv2.waitKey(1) == ord('q'):
    #     break

cap.release()
cv2.destroyAllWindows()
