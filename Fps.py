import cv2
import math

font = cv2.FONT_HERSHEY_COMPLEX_SMALL


def Fps(img, t):
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - t)
    cv2.putText(img, 'FPS: ' + str(int(fps)), (50, 50), font, 1.6, (255, 0, 255), 2)


def drawId(img, x, y, w, h, ids):
    if w >= 40 and h >= 40:
        cv2.putText(img, str(ids), (x + w // 2, y + h // 2), font, 1, (255, 255, 255), 2)


class EuclideanDistTracker:
    def __init__(self):
        # Store the center positions of the objects
        self.center_points = {}
        self.id_count = 0

    def update(self, objects_rect):
        objects_bbs_ids = []

        for rect in objects_rect:
            x, y, w, h = rect
            cx = (x + x + w) // 2
            cy = (y + y + h) // 2

            same_object_detected = False
            for id, pt in self.center_points.items():
                dist = math.hypot(cx - pt[0], cy - pt[1])

                if dist < 60:
                    self.center_points[id] = (cx, cy)
                    objects_bbs_ids.append([x, y, w, h, id])
                    same_object_detected = True
                    break

            # New object is detected we assign the ID to that object
            if same_object_detected is False:
                self.center_points[self.id_count] = (cx, cy)
                objects_bbs_ids.append([x, y, w, h, self.id_count])
                self.id_count += 1

        # Clean the dictionary by center points to remove IDS not used anymore
        new_center_points = {}
        for obj_bb_id in objects_bbs_ids:
            _, _, _, _, object_id = obj_bb_id
            center = self.center_points[object_id]
            new_center_points[object_id] = center

        # Update dictionary with IDs not used removed
        self.center_points = new_center_points.copy()
        return objects_bbs_ids
