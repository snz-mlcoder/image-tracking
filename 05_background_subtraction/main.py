import cv2
import numpy as np

# Function to capture and resize a frame
def get_frame(cap, scaling_factor=0.5):
    ret, frame = cap.read()
    if not ret:
        return None
    frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
    return frame

def main():
    cap = cv2.VideoCapture(0)
    scaling_factor = 0.5

    # Create background subtractor object
    bg_subtractor = cv2.bgsegm.createBackgroundSubtractorMOG()

    history = 100  # Number of frames used to build background model

    while True:
        frame = get_frame(cap, scaling_factor)
        if frame is None:
            break

        # Apply background subtraction model
        mask = bg_subtractor.apply(frame, learningRate=1.0/history)

        # Convert mask to 3 channels for visualization
        mask_color = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

        # Highlight moving objects
        result = cv2.bitwise_and(frame, mask_color)

        # Display original frame and result
        cv2.imshow('Input Frame', frame)
        cv2.imshow('Moving Objects', result)

        key = cv2.waitKey(10)
        if key == 27:  # ESC key
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
