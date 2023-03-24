import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Webcam error")

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Not Stream")
        break
    
    cv2.imshow("Image", frame)
    
    cv2.waitKey(1)