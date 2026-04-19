import cv2

def draw_text(frame, text):
    cv2.putText(
        frame,
        text,
        (10, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )
    return frame