import torch
import time
import sys
import cv2
from ultralytics import YOLO

import features


model = YOLO("./train/best_newds.pt")

cap = cv2.VideoCapture(0)
voice = features.Voice() 
controller = features.Controller() 
search_running = False 
loop = True 

features.Display.processbar("Starting...", 0.65)


while loop:
    ret, img = cap.read() 
    if not ret:
        break

    time.sleep(0.5)
    results = model.predict(img, conf=0.80, stream=True, show=False)
    
    for result in results:
        for tensor in result.boxes.cls:
            voice.search(tensor) 
            controller.media_control(tensor)
            
            if torch.allclose(tensor, torch.tensor([2.])): # classe: C -> Encerra o script
                loop = False


features.Display.processbar("Stopping...", 1)
sys.exit("-"*98)
