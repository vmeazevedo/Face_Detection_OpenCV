import cv2
import numpy as np

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

while True:
	_, frame = cap.read()

	cv2.imshow("frame", frame)

	key = cv2.waitKey(1)

	if key == 27:
		break

cap.release()
cv2.destroyAllWindows()