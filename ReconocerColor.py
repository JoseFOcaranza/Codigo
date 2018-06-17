#capturar una imagen
import cv2
import numpy as np
import commands
import sys, time
from time import sleep

#videoCapture=cv2.VideoCapture(0)

#Se inicia la camara
#captura = cv2.VideoCapture(0)
camera= cv2.VideoCapture(0)

#Fotogramas 2
fotograma=1

def get_image():
	#Leer la captura
	retval, im = camera.read()
	return im

def TomarImagen():
	for i in xrange(fotograma):
		camera_capture = get_image()
		localtime = time.asctime( time.localtime(time.time()))
		file = "Captura "
		cv2.imwrite(file + localtime + '.png', camera_capture)
			
#convertir la imagen
while(1):
        _,imagen = camera.read()
        hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

        #buscar objetos verdes
        verde_bajos = np.array([49,50,50])
        verde_altos = np.array([80,255,255])

        mask = cv2.inRange(hsv, verde_bajos, verde_altos)

        #eliminar ruido

        moments = cv2.moments(mask)
        area = moments['m00']

        if(area > 2000000):
                #buscamos los centros
                x = int(moments['m10']/moments['m00'])
                y = int(moments['m01']/moments['m00'])
                #escribimos el valor de los centros
                print "x = ", x
                print "y = ", y
                #dibujamos el centro con un rectangulo
                cv2.rectangle(imagen,(x, y), (x+2, y+2), (0,0,255), 2)
		TomarImagen()
		break
	#resultado=commands.getoutput('/home/pi/Codigo/CapturaImagen.py')
        #mostrar imagen
        cv2.imshow('mask', mask)
        cv2.imshow('camara', imagen)
	#resultado2=commands.getoutput('/home/pi/Codigo/CapturaImagen.py')
        #escape para terminar programa
        tecla = cv2.waitKey(5) & 0xFF

        if tecla == 27:
                break

del(camera)
cv2.destroyAllWindows()
