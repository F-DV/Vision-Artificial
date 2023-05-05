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

##### Imagen a Grises ##########
I_Gris=cv2.cvtColor(Imagen, cv2.COLOR_BGR2GRAY)
print('Imagen en grises')
plt.imshow(I_Gris.astype('uint8'),vmin=0, vmax=255,cmap='gray') #Grafica la imagen en campo de grises
plt.show()
print('')

#=============================================================================
#============= DETECCION HORIZONTAL ==========================
[Fl, Cl]=I_Gris.shape #Genera dos variables para almacenar el número de filas y Columnas 
Resultado_1=np.zeros((Fl,Cl))
#recorriendo filas
for i in range(0, Fl, 1):
  for j in range(0, Cl-1, 1):
    Actual=I_Gris[i,j]
    Siguiente=I_Gris[i,j+1]
    Diferencia=Siguiente-Actual
    Diferencia=abs(Diferencia)
    if Diferencia>=200 and Diferencia<=250:
       Resultado_1[i,j]=255
    else:
       Resultado_1[i,j]=0
   
#Mostrando resultados independientes
print('Resultado')
plt.imshow(Resultado_1.astype('uint8'),vmin=0, vmax=255,cmap='gray') #Grafica la imagen en campo de grises
plt.show()
print('')

#================================================================================0
#=================== DETECCION VERTICAL================================0
#recorriendo columnas
Diferencia=0
Resultado_2=np.zeros((Fl,Cl))
for j in range(0, Cl, 1):
  for i in range(0, Fl-1, 1):
    Actual=I_Gris[i,j]
    Siguiente=I_Gris[i+1,j]
    Diferencia=Siguiente-Actual
    Diferencia=abs(Diferencia)
    if Diferencia>=200 and Diferencia<=250:
      Resultado_2[i,j]=255
    else:
      Resultado_2[i,j]=0

    
#Mostrando resultados independientes
print('Resultado')
plt.imshow(Resultado_2.astype('uint8'),vmin=0, vmax=255,cmap='gray') #Grafica la imagen en campo de grises
plt.show()
print('')

#====================================================================================
#======== UNIR AMBOS RESULTADOS UTILIZANDO PITAGORAS Y NORMALIZANDO ==============
from math import sqrt
Resultado_3=np.zeros((Fl,Cl))
for i in range(0, Fl, 1):
  for j in range(0, Cl, 1):
    Resultado_3[i,j]=sqrt(Resultado_1[i,j]**2+Resultado_2[i,j]**2)

Resultado_3=cv2.normalize(Resultado_3, Resultado_3, 0, 255, norm_type=cv2.NORM_MINMAX)   

    
#Mostrando resultados independientes
print('Resultado')
plt.imshow(Resultado_3.astype('uint8'),vmin=0, vmax=255,cmap='gray') #Grafica la imagen en campo de grises
plt.show()
print('')