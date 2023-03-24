import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    _, frame = cap.read()
    
    cv2.imshow("Imagem", frame)
    
    cv2.waitKey(1)