import cv2
import numpy as np

def start_tracking():
    cap = cv2.VideoCapture(0)
    scaling_factor = 0.5

    num_frames_to_track = 5       # Number of frames to keep motion history
    num_frames_jump = 2           # Detect new features every n frames
    tracking_paths = []           # List to store tracking point paths
    frame_index = 0

    # Parameters for Lucas-Kanade Optical Flow
    tracking_params = dict(
        winSize=(11, 11),
        maxLevel=2,
        criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03)
    )

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Resize and convert to grayscale
        frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        output_img = frame.copy()

        if len(tracking_paths) > 0:
            prev_img, current_img = prev_gray, frame_gray

            # Get the last known points for tracking
            feature_points_0 = np.float32([tp[-1] for tp in tracking_paths]).reshape(-1, 1, 2)

            # Forward tracking
            feature_points_1, _, _ = cv2.calcOpticalFlowPyrLK(prev_img, current_img, feature_points_0, None, **tracking_params)
            # Backward validation
            feature_points_0_rev, _, _ = cv2.calcOpticalFlowPyrLK(current_img, prev_img, feature_points_1, None, **tracking_params)

            # Check consistency between forward and backward flow
            diff = abs(feature_points_0 - feature_points_0_rev).reshape(-1, 2).max(-1)
            good_points = diff < 1

            new_tracking_paths = []
            for tp, (x, y), good_flag in zip(tracking_paths, feature_points_1.reshape(-1, 2), good_points):
                if not good_flag:
                    continue
                tp.append((x, y))
                if len(tp) > num_frames_to_track:
                    del tp[0]
                new_tracking_paths.append(tp)

                # Draw tracked point
                cv2.circle(output_img, (int(x), int(y)), 3, (0, 255, 0), -1)

            tracking_paths = new_tracking_paths

            # Draw tracking paths
            cv2.polylines(output_img, [np.int32(tp) for tp in tracking_paths], False, (0, 150, 0))

        # Detect new feature points periodically
        if not frame_index % num_frames_jump:
            mask = np.full_like(frame_gray, 255)
            for x, y in [np.int32(tp[-1]) for tp in tracking_paths]:
                cv2.circle(mask, (x, y), 6, 0, -1)

            # Use Shi-Tomasi corner detector to find good features
            feature_points = cv2.goodFeaturesToTrack(
                frame_gray,
                mask=mask,
                maxCorners=500,
                qualityLevel=0.3,
                minDistance=7,
                blockSize=7
            )

            # Add new points to tracking paths
            if feature_points is not None:
                for x, y in np.float32(feature_points).reshape(-1, 2):
                    tracking_paths.append([(x, y)])

        frame_index += 1
        prev_gray = frame_gray

        # Show the result
        cv2.imshow('Optical Flow - Feature Tracking', output_img)

        # Exit on ESC key
        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    start_tracking()
