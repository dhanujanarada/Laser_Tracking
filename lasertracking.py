import cv2
import numpy as np


def track_laser():
    cap = cv2.VideoCapture(0)

    while True:
        # Take each frame
        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_red = np.array([0, 0, 255])
        upper_red = np.array([255, 255, 255])
        mask = cv2.inRange(hsv, lower_red, upper_red)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            max_contour = max(contours, key=cv2.contourArea)
            (x, y), radius = cv2.minEnclosingCircle(max_contour)
            center = (int(x), int(y))
            radius = int(radius)
            cv2.circle(frame, center, radius, (255, 0, 0), 2)

        cv2.imshow("Track Laser", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    track_laser()
