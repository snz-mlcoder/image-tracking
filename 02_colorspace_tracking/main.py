import cv2
import numpy as np

# Capture and resize frame
def get_frame(cap, scaling_factor):
    ret, frame = cap.read()
    if not ret:
        return None
    frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
    return frame

def main():
    cap = cv2.VideoCapture(0)
    scaling_factor = 0.5

    while True:
        frame = get_frame(cap, scaling_factor)
        if frame is None:
            break

        # Convert frame to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define blue color range in HSV
        lower_blue = np.array([100, 150, 50])
        upper_blue = np.array([140, 255, 255])

        # Create mask and apply to frame
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        res = cv2.bitwise_and(frame, frame, mask=mask)
        res = cv2.medianBlur(res, 5)

        # Resize result to match frame size if needed
        res = cv2.resize(res, (frame.shape[1], frame.shape[0]))

        # Combine original and result side by side
        combined = np.hstack((frame, res))

        # Show in one window
        cv2.imshow('Original + Color Detection', combined)

        # Exit on ESC
        key = cv2.waitKey(5)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
