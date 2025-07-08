# 🖼️ Frame Differencing - Motion Detection

This project demonstrates a basic motion detection method using **frame differencing** with a webcam. It is the first step in an image tracking series that will include more advanced techniques.

---

## 📌 How it Works

Frame differencing highlights regions where motion occurs by comparing three consecutive grayscale frames:

1. Compute the absolute difference between `next_frame` and `current_frame`.
2. Compute the absolute difference between `current_frame` and `prev_frame`.
3. Apply a bitwise **AND** to focus on consistent motion.
4. Use **thresholding** to enhance visibility of movement.

---

## 🛠️ Requirements

- Python 3.x  
- OpenCV

Install dependencies with:

```bash
pip install opencv-python


Output Preview
The result will be a black-and-white image where white pixels indicate motion:

[webcam feed showing moving objects in white, static areas in black]
