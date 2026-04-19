import cv2
import numpy as np

def segment_hand(frame):
    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Skin color range
    lower = np.array([0, 20, 70], dtype=np.uint8)
    upper = np.array([20, 255, 255], dtype=np.uint8)

    mask = cv2.inRange(hsv, lower, upper)

    # Blur to reduce noise
    mask = cv2.GaussianBlur(mask, (5, 5), 0)

    return mask


def get_contour(mask):
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) == 0:
        return None

    # Largest contour = hand
    return max(contours, key=cv2.contourArea)