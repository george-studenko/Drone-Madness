import cv2
import matplotlib.pyplot as plt

from YOLO_utils import *
from darknet import Darknet

class Objects_Detected():
    classes = []
    probs = []
    boxes[]
    

def detect(img_path):
    #YOLO config file
    cfg_file = './cfg/yolov3.cfg'

    # Pre-trained weights file
    weight_file = './weights/yolov3.weights'

    # COCO object classes file
    namesfile = 'data/coco.names'

    # YOLO Network architecture
    m = Darknet(cfg_file)

    # Load the pre-trained weights
    m.load_weights(weight_file)

    # Load the COCO object classes
    class_names = load_class_names(namesfile)
    
    img = cv2.imread(img_path)
    original_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Resize the image to the input width and height of the first layer of the network.    
    resized_image = cv2.resize(original_image, (m.width, m.height))

    # Set the NMS threshold
    nms_thresh = 0.6

    # Set the IOU threshold
    iou_thresh = 0.4

    # Detect objects in the image
    boxes = detect_objects(m, resized_image, iou_thresh, nms_thresh)

    # Print the objects found and the confidence level
    print_objects(boxes, class_names)

    #Plot the image with bounding boxes and corresponding object class labels
    plot_boxes(original_image, boxes, class_names, plot_labels = True)