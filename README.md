# What is FruitWeight ?
FruitWeight is an application that can detect fruits on trees (Apples for now ) and count the total number present, in order to calculate their weight at first , then estimate a total price of the detected product.
# How is this useful ?
FruitWeight can provide a big help to people looking to estimate their total income based on the products they have (In a farm for example). Instead of basing the price estimation on previous years, which can change significantly over a year and be misleading, they can use the app to have better insights and estimations , giving them a better vision of their business and maybe even plan their next business plan.
# How does it work ?
The user can either take pictures of trees (as many as he wants) and upload them to the app or use his camera for realtime detection (to be added later). The app will then apply object detection models on the picture in order to detect and count the number of fruit on the tree.
Once the detection is done  , the app will apply weight estimation models based on the fruit detected. Once we get the estimated weight , we can then apply math equations to calculate and estimate the total price of the detected product.
# what models can we possibly use?
- ## EfficientDet ( & EfficientDet-Lite variants )
  EfficientDet is  family of lightweight and efficient object detection models. It's designed to balance accuracy and speed, making it suitable for real-time applications on various devices.
  EfficientDet-Lite is a variant that takes the efficiency aspect even further by targeting mobile and edge devices. It's designed to be more lightweight, making it suitable for devices with lower computational power and memory.
  - Advantages : EfficientDet models are known for their scalability and efficiency. They can provide good accuracy while still maintaining real-time capabilities.
    
- ## YOLOv4
  YOLOv4 is a state-of-the-art object detection model that offers improved accuracy compared to previous YOLO versions. It's capable of detecting small objects like apples on trees. altough,YOLOv4 might be more resource-intensive, which could impact real-time performance on certain devices.
  - Advantages: YOLOv4 provides high accuracy and is well-suited for scenarios where precision is crucial.
 
- ## SSD MobileNetV2
