#Algoritmo para detección de bordes
import cv2 # OpenCV para computer vision
import numpy as np # Para cálculo de matrices
import matplotlib.pyplot as plt #Para graficar
import os #Habilita el manejo de directorios

#Leyendo y mostrando imagen  con ruido
Ruta = r'/home/felipeqg/Documents/Vision-Artificial/assets/images/Lena.png'#Ubicación de la imagen desde el google drive
Imagen = cv2.imread(Ruta)#Lee
Imagen=Imagen[:,:,[2,1,0]]#Organiza
print('Mostrando imagen de referencia')
plt.imshow(Imagen.astype('uint8'),vmin=0, vmax=255) #Muestra
plt.show()
print('')

#==========Imagen a Grises===============
I_Gris=cv2.cvtColor(Imagen, cv2.COLOR_BGR2GRAY)
print('Imagen en grises')
plt.imshow(I_Gris.astype('uint8'),vmin=0, vmax=255,cmap='gray') #Grafica la imagen en campo de grises
plt.show()
print('')

Resultado_Canny = cv2.Canny(I_Gris,130,150)# 130 diferencia mínima, 140 es diferencia màxima

print('Resultado Canny')
plt.imshow(Resultado_Canny.astype('uint8'),vmin=0, vmax=255,cmap='gray') #Grafica la imagen en campo de grises
plt.show()
print('')