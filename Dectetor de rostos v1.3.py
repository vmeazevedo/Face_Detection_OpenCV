import numpy as np
import cv2

cap = cv2.VideoCapture(0)

#Carrega o arquivo Cascade salvos no diretório
face_cascade = cv2.CascadeClassifier('C:\\Users\\pqcir\\Documents\\Python\\detect\\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\\Users\\pqcir\\Documents\\Python\\detect\\haarcascade_eye.xml')

while(True):
	#Lê o frame da câmera
	_, frame = cap.read()
	#Converte para escala de cinz
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#Detecta as faces
	faces = face_cascade.detectMultiScale(gray,1.3,5)
	#Desenha um retângulo ao redor de cada face
	for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = frame[y:y+h, x:x+w]
		#Desenha um retângulo ao redor dos olhos
		eyes = eye_cascade.detectMultiScale(roi_gray)
		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
	# Display
	cv2.imshow('frame',frame)
	#Para se o botão ESC é pressionado
	key = cv2.waitKey(1)
	if key == 27:
		break
#Libera a captura do video do objeto
cap.release()
cv2.destroyAllWindows()