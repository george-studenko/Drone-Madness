import cv2
from YOLO_utils import *
import numpy as np

# Tiny YOLO
weights = 'TinyYolo/yolov2-tiny.weights'
model = 'TinyYolo/yolov2-tiny.cfg'

# YOLO V3
#weights = './weights/yolov3.weights'
#model = './cfg/yolov3.cfg'

min_confidence = 0.5
namesfile = 'data/coco.names'
class_names = load_class_names(namesfile)

net = cv2.dnn.readNetFromDarknet(model, weights)

img = cv2.imread('img/city.jpg')
blob = cv2.dnn.blobFromImage(img, 1.0/255.0, (416,416), True, crop = False)

net.setInput(blob)

detections = net.forward()
#print(detections[:][5:])

for i in np.arange(0, detections.shape[0]):
    scores = detections[i][5:]
    classId = np.argmax(scores)
    #print(classId)
    confidence = scores[classId]

    if confidence > 0.1:
        idx = int(classId)
        print(class_names[idx],confidence)
        #if CLASSES[idx] != "person":
        #    continue

        center_x = int(detections[i][0] * 416)
        center_y = int(detections[i][1] * 416)
        width = int(detections[i][2] * 416)
        height = int(detections[i][3] * 416)
        left = int(center_x - width / 2)
        top = int(center_y - height / 2)
        right = width + left - 1
        bottom = height + top - 1

        box = [left, top, width, height]
        (startX, startY, endX, endY) = box



#print(detections[1][5:])


