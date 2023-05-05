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

sobelX = cv2.Sobel(I_Gris,cv2.CV_64F,1,0)#x gradiente de dirección
sobelY = cv2.Sobel(I_Gris,cv2.CV_64F,0,1)#y gradiente de dirección
 
sobelX = np.uint8(np.absolute(sobelX))#x valor absoluto
sobelY = np.uint8(np.absolute(sobelY))#y valor absoluto

print('Resultado X')
plt.imshow(sobelX.astype('uint8'),vmin=0, vmax=255,cmap='gray') #Grafica la imagen en campo de grises
plt.show()
print('')

#Mostrando resultados independientes
print('Resultado Y')
plt.imshow(sobelY.astype('uint8'),vmin=0, vmax=255,cmap='gray') #Grafica la imagen en campo de grises
plt.show()
print('')

sobelTotal = cv2.bitwise_or(sobelX,sobelY)#
print('Resultado final')
plt.imshow(sobelTotal.astype('uint8'),vmin=0, vmax=255,cmap='gray') #Grafica la imagen en campo de grises
plt.show()
print('')

