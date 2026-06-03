import cv2
from deepface import DeepFace
import csv
import os
from datetime import datetime

known_image_path = "shane.jpg"
attendance_file = "attendance.csv"

if not os.path.exists(attendance_file):
    with open(attendance_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Date", "Time"])

def already_marked(name):
    today = datetime.now().strftime("%Y-%m-%d")
    with open(attendance_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == name and row[1] == today:
                return True
    return False

def mark_attendance(name):
    if not already_marked(name):
        with open(attendance_file, 'a', newline='') as f:
            writer = csv.writer(f)
            now = datetime.now()
            writer.writerow([name, now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S")])
        return True
    return False

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imwrite("temp.jpg", frame)

    try:
        result = DeepFace.verify("temp.jpg", known_image_path, enforce_detection=False)

        if result["verified"]:
            marked = mark_attendance("Shane")
            if marked:
                label = "Shane - Attendance Marked!"
                color = (0, 255, 0)
            else:
                label = "Shane - Already Marked Today"
                color = (255, 255, 0)
        else:
            label = "Unknown"
            color = (0, 0, 255)

    except:
        label = "Detecting..."
        color = (255, 255, 0)

    cv2.putText(frame, label, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
    cv2.imshow('Attendance', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
os.remove("temp.jpg")