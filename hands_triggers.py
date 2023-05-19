from ultralytics import YOLO
import time
import cv2

import features



model = YOLO(r"D:\Projetos\Hand-Signals\train\best_low_res.pt")
cap = cv2.VideoCapture(0)
voice = features.Voice()
controller = features.Controller()
pesquisa_executando = False
processo = None
features.Display.processbar("Iniciando...", 0.65)



while True:
    
    # Lendo cada frame do vídeo
    ret, img = cap.read()
    if not ret:
        break

    # Executando a predição com o modelo YOLO
    time.sleep(0.5)
    results = model.predict(img,  conf=0.90, stream=True, show=False)

    for result in results:
        #box.append(result.boxes.cls)
        for tensor in result.boxes.cls:
            voice.search(tensor)
            controller.media_control(tensor)
