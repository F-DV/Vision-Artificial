
import cv2 # OpenCV para computer vision
import numpy as np # Para cálculo de matrices
import matplotlib.pyplot as plt #Para graficar
import os #Habilita el manejo de directorios

#Leyendo imagen de entrada en HSV
Ruta = r'/home/felipeqg/Documents/Vision-Artificial/assets/images/rubik.png' #Ubicación de la imagen desde el google drive
Imagen = cv2.imread(Ruta)#Lee

#Transformando del canal de color RGB al HSV
Imagen_hsv = cv2.cvtColor(Imagen,cv2.COLOR_BGR2HSV)
Hue=Imagen_hsv[:,:,0]
Saturation=Imagen_hsv[:,:,1]
Value=Imagen_hsv[:,:,2]

# Imagen Original
print('Mostrando imagen de entrada')
plt.imshow(Imagen_hsv.astype('uint8'),vmin=0, vmax=255) #Muestra
plt.show()
print('')



print('Mostrando imagen de entrada')
plt.imshow(Imagen[:,:,[2,1,0]].astype('uint8'),vmin=0, vmax=255) #Muestra
plt.show()
print('')
