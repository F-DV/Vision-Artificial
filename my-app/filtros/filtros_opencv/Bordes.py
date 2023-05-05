#Algoritmo para filtrado prromedio según número de vecinos
import cv2 # OpenCV para computer vision
import numpy as np # Para cálculo de matrices
import matplotlib.pyplot as plt #Para graficar
import os #Habilita el manejo de directorios

#Leyendo y mostranso imagen  con ruido
Ruta = r'/home/felipeqg/Documents/Vision-Artificial/assets/images/imagen_1.JPG'#Ubicación de la imagen desde el google drive
Imagen = cv2.imread(Ruta)#Lee
Imagen=Imagen[:,:,[2,1,0]]#Organiza
print('Mostrando imagen con ruido')
plt.imshow(Imagen.astype('uint8'),vmin=0, vmax=255) #Muestra
plt.figure(figsize=(20,20))
plt.show()
print('')
#=============================================================================
#Mejorando problemas de ruido con tres filtros
Resultado_1 = cv2.blur(Imagen,(9,9)) #Filtro promedio
print('Imagen mejorada 1')
plt.imshow(Resultado_1.astype('uint8'),vmin=0, vmax=255) #Grafica la imagen
plt.figure(figsize=(20,20))
plt.show()
print('')

Resultado_2 = cv2.GaussianBlur(Imagen,(9,9),0) #Filtro Gaussiano
print('Imagen mejorada 2')
plt.imshow(Resultado_2.astype('uint8'),vmin=0, vmax=255) #Grafica la imagen
plt.figure(figsize=(20,20))
plt.show()

Resultado_3 = cv2.medianBlur(Imagen,9) #Filtro de la mediana
print('Imagen mejorada 3')
plt.imshow(Resultado_3.astype('uint8'),vmin=0, vmax=255) #Grafica la imagen
plt.figure(figsize=(20,20))
plt.show()
print('')


kernel_1 = np.array(([-1,-1,-1],[-1,8,-1],[-1,-1,-1]),dtype='float')

Resultado = cv2.filter2D(Resultado_3,-1,kernel_1)

print('Imagen mejorada 1')
plt.imshow(Resultado.astype('uint8'),vmin=0, vmax=255) #Grafica la imagen
plt.show()
print('')