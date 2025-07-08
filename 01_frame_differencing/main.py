import cv2

def frame_diff(prev_frame, cur_frame, next_frame):
    # Compute absolute differences between frames
    diff_frames1 = cv2.absdiff(next_frame, cur_frame)
    diff_frames2 = cv2.absdiff(cur_frame, prev_frame)

    # Combine differences using bitwise AND to focus on real motion
    diff = cv2.bitwise_and(diff_frames1, diff_frames2)

    # Apply binary threshold to highlight moving areas
    _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

    return thresh

# Capture and preprocess a frame
def get_frame(cap, scaling_factor):
    ret, frame = cap.read()
    if not ret:
        return None
    # Resize the frame
    frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
    # Convert to grayscale
    return cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

def main():
    cap = cv2.VideoCapture(0)
    scaling_factor = 0.5

    prev_frame = get_frame(cap, scaling_factor)
    cur_frame = get_frame(cap, scaling_factor)
    next_frame = get_frame(cap, scaling_factor)

    while True:
        # Compute and display frame difference
        diff = frame_diff(prev_frame, cur_frame, next_frame)
        cv2.imshow("Object Movement", diff)

        # Update frame variables
        prev_frame = cur_frame
        cur_frame = next_frame
        next_frame = get_frame(cap, scaling_factor)

        # Exit if ESC key is pressed
        key = cv2.waitKey(10)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
