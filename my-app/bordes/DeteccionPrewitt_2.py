#Algoritmo para detección de bordes con PREWITT

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

#=======Imagen a gris==========
I_Gris=cv2.cvtColor(Imagen, cv2.COLOR_BGR2GRAY)
print('Imagen en grises')
plt.imshow(I_Gris.astype('uint8'),vmin=0, vmax=255,cmap='gray') #Grafica la imagen en campo de grises
plt.show()
print('')

#Detectando bordes Prewitt
from math import sqrt
[Fl, Cl]=I_Gris.shape #Genera dos variables para almacenar el número de filas y Columnas 
Resultado_X=np.zeros((Fl,Cl))
Resultado_Y=np.zeros((Fl,Cl))
Resultado_X2=np.zeros((Fl,Cl))
Resultado_Y2=np.zeros((Fl,Cl))

Resultado_Total=np.zeros((Fl,Cl))
#Crea kernels Prewitt manualmente
kernel_x = np.array(([-1,0,1],[-1,0,1],[-1,0,1]),dtype='float')
kernel_y = np.array(([-1,-1,-1],[0,0,0],[1,1,1]),dtype='float')
kernel_x2 = np.array(([1,0,-1],[1,0,-1],[1,0,-1]),dtype='float')
kernel_y2 = np.array(([1,1,1],[0,0,0],[-1,-1,-1]),dtype='float')


#Corriendo filtros
Resultado_X = cv2.filter2D(I_Gris,-1,kernel_x)
Resultado_Y = cv2.filter2D(I_Gris,-1,kernel_y)
Resultado_X2 = cv2.filter2D(I_Gris,-1,kernel_x2)
Resultado_Y2 = cv2.filter2D(I_Gris,-1,kernel_y2)


#Mostrando resultados independientes
print('Resultado X')
plt.imshow(Resultado_X.astype('uint8'),vmin=0, vmax=255,cmap='gray') #Grafica la imagen en campo de grises
plt.show()
print('')

#Mostrando resultados independientes
print('Resultado X2')
plt.imshow(Resultado_X2.astype('uint8'),vmin=0, vmax=255,cmap='gray') #Grafica la imagen en campo de grises
plt.show()
print('')

#Mostrando resultados independientes
print('Resultado Y')
plt.imshow(Resultado_Y.astype('uint8'),vmin=0, vmax=255,cmap='gray') #Grafica la imagen en campo de grises
plt.show()
print('')

#Mostrando resultados independientes
print('Resultado Y2')
plt.imshow(Resultado_Y2.astype('uint8'),vmin=0, vmax=255,cmap='gray') #Grafica la imagen en campo de grises
plt.show()
print('')


# Calculando resultado total
for i in range(0, Fl, 1):
  for j in range(0, Cl, 1):
    Resultado_Total[i,j]=sqrt((Resultado_X[i,j]/6)**2+(Resultado_Y[i,j]/6)**2+(Resultado_X2[i,j]/6)**2+(Resultado_Y2[i,j]/6)**2)

# Normalizando resultados
Resultado_Total=cv2.normalize(Resultado_Total, Resultado_Total, 0, 255, norm_type=cv2.NORM_MINMAX)  

#Mostrando resultados independientes
print('Resultado final')
plt.imshow(Resultado_Total.astype('uint8'),vmin=0, vmax=255,cmap='gray') #Grafica la imagen en campo de grises
plt.show()
print('')