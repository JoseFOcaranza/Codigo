import cv2
import numpy as np

imagen=cv2.imread('Captura.png')
hsv= cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

"""
Rango de colores detectados
verdes
"""

verdes_bajos= np.array([49,50,50])
verdes_altos= np.array([107,255,255])

#Ahora los azules 
azul_bajos = np.array([100,65,75], dtype=np.uint8)
azul_altos = np.array([130,255,255], dtype=np.uint8)

#Rojos
rojos_bajos1 = np.array([0,65,75], dtype=np.uint8)
rojos_altos1 = np.array([12,255,255], dtype=np.uint8)
rojos_bajos2 = np.array([240,65,75], dtype=np.uint8)
rojos_altos2 = np.array([256,255,255], dtype=np.uint8)
#Crear las mascaras
mascara_verde = cv2.inRange(hsv, verdes_bajos, verdes_altos)
mascara_rojo1 = cv2.inRange(hsv, rojos_bajos1, rojos_altos1)
mascara_rojo2 = cv2.inRange(hsv, rojos_bajos2, rojos_altos2)
mascara_azul = cv2.inRange(hsv, azul_bajos, azul_altos)

#Juntar las  mascaras para crear la matrix
mask = cv2.add(mascara_rojo1, mascara_rojo2)
mask = cv2.add(mask, mascara_verde)
mask = cv2.add(mask, mascara_azul)

#Mostrar la imagen inicial y pulsar esc
cv2.imshow('finale', mask)
cv2.imshow('imagen', imagen)
#Para abortar mission
while (1):
	tecla = cv2.waitKey(5) &  0xFF 
	if tecla == 27:
		break
cv2.destroyAllWindows()




