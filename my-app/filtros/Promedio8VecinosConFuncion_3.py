#Algoritmo para 8 vecinos
import cv2 # OpenCV para computer vision
import numpy as np # Para cálculo de matrices
import matplotlib.pyplot as plt #Para graficar
import os #Habilita el manejo de directorios

#=============================================================================
#Definiendo función para mejora de ruido basada en promedio de ocho vecinos
def O_vecinos(Imagen):
  global Resultado
  [Fl, Cl, Ch]=Imagen.shape #Genera dos variables para almacenar el número de filas y Columnas 
  Resultado=np.zeros((Fl,Cl,Ch))

  for k in range(0, Ch, 1):
    for j in range(1, Cl-1, 1):
      for i in range(1, Fl-1, 1):
        Sup=float(Imagen[i-1,j,k])
        Sup_I=float(Imagen[i-1,j-1,k])
        Sup_D=float(Imagen[i-1,j+1,k])
        Inf=float(Imagen[i+1,j,k])
        Inf_D=float(Imagen[i+1,j+1,k])
        Inf_I=float(Imagen[i+1,j-1,k])
        Der=float(Imagen[i,j+1,k])
        Izq=float(Imagen[i,j-1,k])
      
        Resultado[i,j,k]= (Sup + Sup_I + Sup_D + Inf + Inf_D + Inf_I + Der + Izq)/8

        if Resultado[i,j,k]>255:
          Resultado[i,j,k]=255

        if Resultado[i,j,k]<0:
           Resultado[i,j,k]=0
#=============================================================================

#Leyendo y mostranso imagen de referencia con ruido
Ruta_2 = r'//home/felipeqg/Documents/Vision-Artificial/assets/images/Parcial_1_B.jpg'#Ubicación de la imagen desde el google drive
Imagen_2 = cv2.imread(Ruta_2)#Lee
Imagen_2=Imagen_2[:,:,[2,1,0]]#Organiza
print('Mostrando imagen con ruido')
plt.imshow(Imagen_2.astype('uint8'),vmin=0, vmax=255) #Muestra
plt.show()
print('')

#=============================================================================
#Mejorando problemas de ruido con 8 vecinos
Resultado=Imagen_2
for veces in range(0,10,1):
  O_vecinos(Resultado)
  print('Imagen mejorada', veces+1, 'veces')
  plt.imshow(Resultado.astype('uint8'),vmin=0, vmax=255) #Grafica la imagen en campo de grises
  plt.show()
  print('')