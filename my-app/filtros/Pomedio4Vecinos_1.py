# FILTROS CON UN KERNEL LAS VECINDADES
# PROMEDIOS DE VECINOS
# FILTRO DE PORCENTAGE (MATRIZ CONVOLUCION)

#Algoritmo para 4 vecinos
import cv2 # OpenCV para computer vision
import numpy as np # Para cálculo de matrices
import matplotlib.pyplot as plt #Para graficar
import os #Habilita el manejo de directorios

#=============================================================================
#Leyendo y mostrando imagen de referencia con ruido
Ruta_2 = r'/home/felipeqg/Documents/Vision-Artificial/assets/images/Parcial_1_B.jpg'#Ubicación de la imagen desde el google drive
Imagen_2 = cv2.imread(Ruta_2)#Lee
Imagen_2=Imagen_2[:,:,[2,1,0]]#Organiza
print('Mostrando imagen con ruido')
plt.imshow(Imagen_2.astype('uint8'),vmin=0, vmax=255) #Muestra
plt.show()
print('')



#=============================================================================
#Mejorando problemas de ruido con 4 vecinos

[Fl, Cl, Ch]=Imagen_2.shape #Genera dos variables para almacenar el número de filas y Columnas 
Resultado=np.zeros((Fl,Cl,Ch))

for k in range(0, Ch, 1):#Canales
  for j in range(1, Cl-1, 1):#Columnas
    for i in range(1, Fl-1, 1):#Filas
      Sup=float(Imagen_2[i-1,j,k]) #Arriba
      Inf=float(Imagen_2[i+1,j,k]) #Abajo
      Der=float(Imagen_2[i,j+1,k]) #Derecha
      Izq=float(Imagen_2[i,j-1,k]) #Inzquierda

      Resultado[i,j,k]= (Sup + Inf + Der + Izq)/4

      if Resultado[i,j,k]>255:
         Resultado[i,j,k]=255
  
      if Resultado[i,j,k]<0:
         Resultado[i,j,k]=0

print('Imagen mejorada')
plt.imshow(Resultado.astype('uint8'),vmin=0, vmax=255) #Grafica la imagen
plt.show()
print('')

