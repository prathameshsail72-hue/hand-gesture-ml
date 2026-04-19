import cv2
import numpy as np

def count_fingers(contour):
    hull = cv2.convexHull(contour, returnPoints=False)

    if hull is None or len(hull) < 3:
        return 0

    defects = cv2.convexityDefects(contour, hull)

    if defects is None:
        return 0

    count = 0

    for i in range(defects.shape[0]):
        s, e, f, d = defects[i][0]
        start = tuple(contour[s][0])
        end = tuple(contour[e][0])
        far = tuple(contour[f][0])

        a = np.linalg.norm(np.array(end) - np.array(start))
        b = np.linalg.norm(np.array(far) - np.array(start))
        c = np.linalg.norm(np.array(end) - np.array(far))

        # cosine rule
        angle = np.arccos((b**2 + c**2 - a**2) / (2*b*c))

        if angle <= np.pi / 2:
            count += 1

    return count


def classify_gesture(finger_count):
    if finger_count == 0:
        return "Fist ✊"
    elif finger_count == 1:
        return "One ☝️"
    elif finger_count == 2:
        return "Two ✌️"
    elif finger_count == 4:
        return "Open Hand ✋"
    else:
        return "Unknown"