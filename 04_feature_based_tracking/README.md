#  Feature-Based Tracking with Optical Flow (Lucas-Kanade)

This project demonstrates how to track feature points in a video using **Lucas-Kanade Optical Flow**, a widely used technique in computer vision.

---

##  How It Works

- Detect good features using `cv2.goodFeaturesToTrack`.
- Track them across frames using **Pyramidal Lucas-Kanade Optical Flow** (`cv2.calcOpticalFlowPyrLK`).
- Use forward-backward error to validate matches.
- Draw **motion paths** and live feature points.

---

##  Key Concepts

- Feature points (corners) are selected and tracked across frames.
- Motion vectors (trajectories) are drawn for each point.
- Every few frames, new features are added to maintain robust tracking.

---

## ▶ Run

```bash
python main.py
