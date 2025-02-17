import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    _, frame= cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_green=np.array([35, 100, 100])
    upper_green=np.array([85,255,255])

    mask=cv2.inRange(hsv,lower_green, upper_green)
    result=cv2.bitwise_and(frame, frame, mask=mask)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) > 100:  # Filter small areas
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 5)
            cv2.putText(frame, 'Object Berwarna Hijau', (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)

    if cv2.waitKey(1)& 0xFF == ord('q'):

        break

cap.release()
cv2.destroyAllWindows()