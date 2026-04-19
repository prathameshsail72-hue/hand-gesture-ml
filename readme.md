# 🖐️ Hand Gesture Recognition using OpenCV

## 📌 Overview

This project implements a **real-time hand gesture recognition system** using computer vision techniques.
Unlike many implementations, this project does **not rely on pre-trained frameworks** and instead uses pure OpenCV-based image processing.

The system detects hand regions, extracts contours, counts fingers, and classifies gestures in real-time using a webcam.

---

## 🚀 Features

* Real-time webcam-based hand detection
* Skin color segmentation using HSV color space
* Contour detection for hand region extraction
* Finger counting using convex hull & convexity defects
* Gesture classification (Fist, One, Two, Open Hand, etc.)
* Clean and modular project structure

---

## 📂 Project Structure

```
hand-gesture-ml/
│
├── src/
│   ├── hand_segmentation.py      # Hand detection using color segmentation
│   ├── gesture_classifier.py    # Finger counting & gesture classification
│   ├── utils.py                 # Helper functions (drawing, etc.)
│
├── app.py                       # Main application (webcam)
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/hand-gesture-ml.git
cd hand-gesture-ml
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the application:

```
python app.py
```

Press:

```
q
```

to exit the application.

---

## 🧠 How It Works

### 1. Hand Segmentation

* Converts frame to HSV color space
* Applies skin color threshold
* Generates a binary mask

### 2. Contour Detection

* Finds contours in the mask
* Selects the largest contour as the hand

### 3. Finger Counting

* Uses convex hull and convexity defects
* Calculates angles between fingers

### 4. Gesture Classification

| Fingers Detected | Gesture     |
| ---------------- | ----------- |
| 0                | Fist ✊      |
| 1                | One ☝️      |
| 2                | Two ✌️      |
| 4                | Open Hand ✋ |

---

## 📸 Demo

*Add screenshots or GIFs here showing:*

* Hand detection
* Mask output
* Gesture recognition

---

## ⚠️ Limitations

* Sensitive to lighting conditions
* Skin color detection may vary across users
* Accuracy depends on background simplicity
* Basic rule-based gesture classification

---

## 🔮 Future Improvements

* Improve hand segmentation using YCbCr color space
* Add machine learning-based gesture classification
* Map gestures to system actions (volume, cursor control)
* Build a web interface using Streamlit
* Add support for multiple hands

---

## 🧪 Tech Stack

* Python
* OpenCV
* NumPy

---

## 🤝 Contributing

Contributions are welcome!
Feel free to open issues or submit pull requests.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

Prathamesh Sail
GitHub: https://github.com/prathameshsail72-hue
