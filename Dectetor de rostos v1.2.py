import cv2

#Carrega o arquivo Cascade salvo no diretório
face_cascade = cv2.CascadeClassifier('C:\\Users\\pqcir\\Documents\\Python\\detect\\haarcascade_frontalface_default.xml')
#Faz a leitura da imagem no diretório
img = cv2.imread('C:\\Users\\pqcir\\Documents\\Python\\detect\\quad2.jpg')
#Converte para escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Detecta as faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
#Desenha um retângulo ao redor das faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
#Apresenta a saída
cv2.imshow('img', img)
cv2.waitKey()