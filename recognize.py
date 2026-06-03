import cv2
from deepface import DeepFace
import os

known_image_path = "shane.jpg"

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    cv2.imwrite("temp.jpg", frame)
    
    try:
        result = DeepFace.verify("temp.jpg", known_image_path, enforce_detection=False)
        
        if result["verified"]:
            label = "Shane - Verified"
            color = (0, 255, 0)
        else:
            label = "Unknown"
            color = (0, 0, 255)
            
    except:
        label = "Detecting..."
        color = (255, 255, 0)
    
    cv2.putText(frame, label, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    cv2.imshow('Recognition', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
os.remove("temp.jpg")