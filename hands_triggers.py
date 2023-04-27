from ultralytics import YOLO
import subprocess
import time
import torch
import cv2

model = YOLO(r"D:\Projetos\Hand-Signals\train\best_cuda.pt")

cap = cv2.VideoCapture(0)

cont = 0

while True:
    
    # Lendo cada frame do vídeo
    ret, img = cap.read()
    if not ret:
        break

    with torch.no_grad():
        # Executando a predição com o modelo YOLO
        results_v = model.predict(img,  conf=0.65, classes=21, show=True)
        results_w = model.predict(img,  conf=0.65, classes=22, show=True)
    
    for result in results_v:
        #box.append(result.boxes.cls)
        for tensor in result.boxes.cls:
            if torch.allclose(tensor, torch.tensor([21.])):
                cont += 1
                if cont == 1:
                    processo = subprocess.Popen(['notepad.exe', 'D:\Projetos\Teste\meabra.txt'])
                    pass
                    #processo.wait()

    for result_w in results_w:
        #box.append(result.boxes.cls)
        for tensor_w in result_w.boxes.cls:
            if torch.allclose(tensor_w, torch.tensor([22.])):
                processo.terminate() # fecha o programa
                cont = 0
                break


    # # Exibindo a imagem na janela
    # cv2.imshow("YOLOv8", img)
    
    # Aguardando a tecla 'q' para finalizar a execução
    if cv2.waitKey(1) == ord('q'):
        break

#print(box)

cap.release()
cv2.destroyAllWindows()