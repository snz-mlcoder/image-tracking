#  Background Subtraction (MOG)

This project demonstrates **background subtraction** using OpenCV's **MOG (Mixture of Gaussians)** model. It helps detect moving objects in a mostly static scene, commonly used in video surveillance.

---

##  How It Works

- A background model is built and continuously updated over time.
- Each new frame is compared with this model to detect **foreground motion**.
- Foreground objects (i.e., motion) are extracted using `cv2.bgsegm.createBackgroundSubtractorMOG()`.

---

##  Key Concepts

- **Adaptive learning**: The model gradually updates based on scene changes.
- **Learning rate**: A lower value means faster adaptation to changes.
- **Foreground mask**: White regions = motion; black = background

---

##  Run

```bash
python main.py
