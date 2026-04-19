import pyautogui

def perform_action(gesture):
    if gesture == "Fist ✊":
        pyautogui.press("space")   # Pause/Play

    elif gesture == "One ☝️":
        pyautogui.press("volumeup")

    elif gesture == "Two ✌️":
        pyautogui.press("volumedown")

    elif gesture == "Open Hand ✋":
        pyautogui.press("playpause")

    else:
        pass