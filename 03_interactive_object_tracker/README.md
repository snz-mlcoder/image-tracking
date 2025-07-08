#  Interactive Object Tracker (CAMShift)

This project allows you to **manually select an object** with the mouse and track it in real-time using the **CAMShift algorithm**.

---

## 🖱️ How It Works

1. Click and drag with the mouse to select the object (ROI).
2. The tracker computes a histogram of the selected region.
3. CAMShift tracks the object frame by frame using histogram backprojection.
4. The object is outlined with a green ellipse during tracking.

---

##  Features

- Interactive ROI selection with mouse
- Real-time object tracking using OpenCV’s CAMShift
- Uses HSV color space and masking for robust tracking

---

## ▶ Run

```bash
python main.py
