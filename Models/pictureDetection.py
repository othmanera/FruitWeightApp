import cv2
from ultralytics import YOLO
Model = YOLO('CustomModel.pt')
results=Model("../data/Pictures/10421367345_acb53d968e_z.jpg",show=True)
cv2.waitKey(0)