import cv2
import numpy as np
from ultralytics import YOLO
import cvzone
import math
from .Sort import *

#picture detection
def pictureDetection(filePath):
    Model = YOLO('FruitWeight/Models/YoloWeights/yolov8l.pt')
    results = Model(filePath, show=True)
    return results


#video detection
def videoDetection(filepath):
    # calling the model we are going to use
    model = YOLO("FruitWeight/Models/YoloWeights/yolov8l.pt")

    # using cv2 to capture webcam/video footage
    # cap = cv2.VideoCapture(0) #webcam
    # #setting height/width of the webcam
    # cap.set(3,1280)
    # cap.set(4,720)
    cap = cv2.VideoCapture(filepath)  # video

    classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
                  "traffic light", "fire hydrant",
                  "stop sign", "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep", "cow", "elephant",
                  "bear", "zebra",
                  "giraffe", "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard",
                  "sports ball", "kite",
                  "baseball bat", "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass",
                  "cup", "fork",
                  "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli", "carrot", "hot dog",
                  "pizza", "donut",
                  "cake", "chair", "sofa", "pottedplant", "bed", "diningtable", "toilet", "tvmonitor", "Laptop",
                  "mouse", "remote", "keyboard",
                  "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase",
                  "scissors", "teddy bear",
                  "hair driep", "toothbrush"]

    # tracking
    tracker = Sort(max_age=20, min_hits=3, iou_threshold=0.3)

    activeIds = []  # a list to store the ids of the current (ONLY) objects being tracked

    totalCount = 0  # A counter that keeps track of the number of the objects tracked

    while True:
        success, img = cap.read()
        results = model(img, stream=True)

        detections = np.empty((0, 5))

        for r in results:
            boxes = r.boxes

            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                # cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),3)
                w, h = x2 - x1, y2 - y1
                # cvzone.cornerRect(img, (x1, y1, w, h))

                conf = math.ceil((box.conf[0] * 100) / 100)

                cls = int(box.cls[0])
                currentClass = classNames[cls]

                if currentClass == "apple":
                    # cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(0, y1)))
                    currentArray = np.array([x1, y1, x2, y2, conf])
                    detections = np.vstack((detections, currentArray))

        trackerResults = tracker.update(detections)  # updates the current objects being tracked

        for result in trackerResults:
            x1, y1, x2, y2, id = result
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1

            if id not in activeIds:
                activeIds.append(id)
                totalCount += 1

            print(activeIds)
            cvzone.putTextRect(img, f'{int(id)}', (max(0, x1), max(0, y1)))
            cvzone.cornerRect(img, (x1, y1, w, h))

        cvzone.putTextRect(img, f'{totalCount}', (50, 50))

        cv2.imshow("Image", img)
        cv2.waitKey(1)