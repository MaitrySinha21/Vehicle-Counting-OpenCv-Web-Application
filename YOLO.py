import numpy as np
import cv2

classes = []
with open('coco.names','r') as f:
    classes = [line.strip() for line in f.readlines()]
path = 'traffic1.mp4'
net = cv2.dnn.readNetFromDarknet('yolov4-tiny.cfg','yolov4-tiny.weights')
#detector = cv2.createBackgroundSubtractorMOG2(history=100,varThreshold=40)
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
cap = cv2.VideoCapture(path)
cap.set(10,150)

def Yolo(frame):
    ht, wt, _ = frame.shape
    blob = cv2.dnn.blobFromImage(frame, 1 / 255, (320, 320), (0, 0, 0), swapRB=True, crop=False)
    net.setInput(blob)
    last_layer = net.getUnconnectedOutLayersNames()
    layer_out = net.forward(last_layer)
    boxes = []
    confidences = []
    centroids = []
    cls_ids = []
    for output in layer_out:
        for detection in output:
            score = detection[5:]
            clsid = np.argmax(score)
            conf = score[clsid]
            if conf > 0.4:
                centreX = int(detection[0] * wt)
                centreY = int(detection[1] * ht)
                w = int(detection[2] * wt)
                h = int(detection[3] * ht)
                x = int(centreX - w / 2)
                y = int(centreY - h / 2)
                centroids.append((centreX, centreY))
                boxes.append([x, y, w, h])
                confidences.append((float(conf)))
                cls_ids.append(clsid)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, .3, .2)
    colors = np.random.uniform(0, 255, size=(len(boxes), 2))
    try:
        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            label = str(classes[cls_ids[i]])
            if (label == 'car') or (label == 'bus') or (label == 'truck'):
                confidence = str(round(confidences[i] * 100, 1)) + '%'
                color = colors[i]
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                cv2.putText(frame, label.upper() + "-" + confidence, (x, y - 5), font, 0.7, (0, 255, 255), 1)

    except:
        pass
