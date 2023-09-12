import cv2
from ultralytics import YOLO
Model = YOLO('CustomModel.pt')
results=Model("../data/Pictures/Apple.jpg",show=True)
cv2.waitKey(0)