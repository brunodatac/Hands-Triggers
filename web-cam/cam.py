import cv2

def webcam(cam_number):
    cap = cv2.VideoCapture(cam_number)
    window_name = "Webcam"

    if not cap.isOpened():
        print("Webcam error")
        exit()

    while True:
        ret, frame = cap.read()
        
        if not ret:
            print("Not Stream")
            break
        
        cv2.imshow(window_name, frame)
        
        k = cv2.waitKey(1)
        
        if k == ord('q'):
            break
        
        if cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
            break
        
    cv2.detroyAllWindows()
    cap.release()
    print("Close")