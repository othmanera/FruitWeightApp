import cv2
from ultralytics import YOLO
import cvzone
import math
from Sort import *

# calling the model we are going to use
model = YOLO("CustomModel.pt    ")

# using cv2 to capture webcam/video footage
# cap = cv2.VideoCapture(0) #webcam
# #setting height/width of the webcam
# cap.set(3,1280)
# cap.set(4,720)
cap = cv2.VideoCapture("../Data/videos/ApplesV2.mp4")  # video

classNames = ["apple"]

while True:
    success, img = cap.read()
    results = model(img, stream=True)

    for r in results:
        boxes = r.boxes

        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            # cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),3)
            w, h = x2 - x1, y2 - y1
            cvzone.cornerRect(img, (x1, y1, w, h))

            conf = math.ceil((box.conf[0] * 100) / 100)

            cls = int(box.cls[0])

            cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(0, y1)))

    cv2.imshow("Image", img)
    cv2.waitKey(1)

