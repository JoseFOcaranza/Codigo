import cv2

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
print"Foto tomada"
#Entregar imagen leida anteriormente
camera_capture = get_image()
file = "Captura.png"
#Guardar la imagen con opencv que fue leida por pil
cv2.imwrite(file, camera_capture)
#Finalizar camara
del(camera)
