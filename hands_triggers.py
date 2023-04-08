from ultralytics import YOLO
import torch
import cv2

model = YOLO(r"D:\Projetos\Hand-Signals\train\best_n_50e_8class.pt")

cap = cv2.VideoCapture(0)

# box = []
cont = 0

while True:
    
    # Lendo cada frame do vídeo
    ret, img = cap.read()
    if not ret:
        break
    
    # Executando a predição com o modelo YOLO
    results = model.predict(img,  conf=0.40, classes=21, show=False)
    
    for result in results:
        # box.append(result.boxes.cls)
        for tensor in result.boxes.cls:
            if torch.allclose(tensor, torch.tensor([21.]), atol=1e-5):
                cont += 1


    # Exibindo a imagem na janela
    cv2.imshow("YOLOv8", img)
    
    # Aguardando a tecla 'q' para finalizar a execução
    if cv2.waitKey(1) == ord('q'):
        break

# print(box)
print(cont)
cap.release()
cv2.destroyAllWindows()