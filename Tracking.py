import cv2
from Fps import EuclideanDistTracker
from Fps import drawId
IDS = []
tracking = EuclideanDistTracker()
classes = []

path = 'traffic1.mp4'
detector = cv2.createBackgroundSubtractorMOG2(history=100,varThreshold=40)
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
cap = cv2.VideoCapture(path)
cap.set(10,150)

def Tracking(frame):
    # Extracting region of interest
    roi = frame[320:420, 50:850]
    mask = detector.apply(roi)
    # making NMS
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detect = []
    for cont in contours:
        area = cv2.contourArea(cont)
        # removing small area
        if area > 400:
            x1, y1, w1, h1 = cv2.boundingRect(cont)
            detect.append([x1, y1, w1, h1])

    boxes_ids = tracking.update(detect)
    for box_id in boxes_ids:
        x, y, w, h, ids = box_id
        drawId(roi, x, y, w, h, ids)
        if ids not in IDS:
            IDS.append(ids)

    n = len(IDS)
    cv2.putText(frame, 'Vehicle Crossed: ' + str(n), (50, 90), font, 1.6, (255, 0, 255), 2)
