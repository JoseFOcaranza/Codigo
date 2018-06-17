import cv2
import sys, time
from time import sleep
#Camara 1

camara=0

#Numero de fotogramas
fotograma=1

#Iniciar camara
camera=cv2.VideoCapture(camara)
#Capturar imagen de camara
def get_image():
	#Leer la captura
	retval, im = camera.read()
	return im
for i in xrange(fotograma):
	temp = get_image()
	camera_capture = get_image()
	localtime = time.asctime( time.localtime(time.time()))
	file = "Captura "
 	cv2.imwrite(file + localtime+'.png', camera_capture)

print"Foto tomada"
#Entregar imagen leida anteriormente
#camera_capture = get_image()
#file = "Captura.png"
#Guardar la imagen con opencv que fue leida por pil
#cv2.imwrite(file, camera_capture)
#Finalizar camara
del(camera)
