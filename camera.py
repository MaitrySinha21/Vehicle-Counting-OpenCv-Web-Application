import cv2
from Tracking import Tracking
from Fps import EuclideanDistTracker
from Fps import Fps
from YOLO import Yolo

tracking = EuclideanDistTracker()
classes = []
path = 'traffic1.mp4'
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
cap = cv2.VideoCapture(path)
cap.set(10,150)
IDS = []
class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(path)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        while True:
            try:
                t = cv2.getTickCount()
                _, frame = cap.read()
                frame = cv2.resize(frame, (900, 520))
                ret, frame = self.video.read()
                frame = cv2.resize(frame, (900, 520))
                font = cv2.FONT_HERSHEY_COMPLEX_SMALL
                Tracking(frame)
                Yolo(frame)
                Fps(frame, t)
                cv2.line(frame, (160, 320), (730, 320), (0, 255, 0), 2)
                cv2.line(frame, (0, 420), (900, 420), (0, 255, 0), 2)
                cv2.line(frame, (160, 320), (0, 420), (0, 255, 0), 2)
                cv2.line(frame, (730, 320), (900, 420), (0, 255, 0), 2)
                cv2.imshow('Tracking', frame)

                ret, jpeg = cv2.imencode('.jpg', frame)
                return jpeg.tobytes()

            except:
                ret, jpeg = cv2.imencode('.jpg', frame)
                return jpeg.tobytes()
