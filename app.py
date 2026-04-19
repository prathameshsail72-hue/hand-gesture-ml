import cv2
from src.hand_segmentation import segment_hand, get_contour
from src.gesture_classifier import count_fingers, classify_gesture
from src.utils import draw_text

def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)

        mask = segment_hand(frame)
        contour = get_contour(mask)

        gesture = "No Hand"

        if contour is not None:
            finger_count = count_fingers(contour)
            gesture = classify_gesture(finger_count)

            cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)

        frame = draw_text(frame, gesture)

        cv2.imshow("Hand Gesture Recognition (OpenCV)", frame)
        cv2.imshow("Mask", mask)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()