# 🎨 Colorspace-Based Tracking (HSV Color Detection)

This project demonstrates how to track a specific color (e.g., blue) using the **HSV colorspace** in OpenCV. It's the second project in the image tracking series.

---

## 📌 How It Works

1. Captures webcam video.
2. Converts each frame to HSV.
3. Filters out everything except the target color (blue).
4. Displays both the original frame and the filtered result **side-by-side in one window**.

---

## 🖼️ Output Window

The result shows two images next to each other:
- **Left:** Original webcam frame  
- **Right:** Highlighted areas with the selected color (blue)

---

## 🎯 HSV Color Range Used

```python
lower_blue = np.array([100, 150, 50])
upper_blue = np.array([140, 255, 255])
