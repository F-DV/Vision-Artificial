#Algoritmo para filtrado prromedio según número de vecinos
import cv2 # OpenCV para computer vision
import numpy as np # Para cálculo de matrices
import matplotlib.pyplot as plt #Para graficar
import os #Habilita el manejo de directorios

#Leyendo y mostranso imagen  con ruido
Ruta = r'//home/felipeqg/Documents/Vision-Artificial/assets/images/Parcial_1_B.jpg'#Ubicación de la imagen desde el google drive
Imagen = cv2.imread(Ruta)#Lee
Imagen=Imagen[:,:,[2,1,0]]#Organiza
print('Mostrando imagen con ruido')
plt.imshow(Imagen.astype('uint8'),vmin=0, vmax=255) #Muestra
plt.show()
print('')

#=============================================================================
#Mejorando problemas de ruido 
[Fl, Cl, Ch]=Imagen.shape #Genera dos variables para almacenar el número de filas y Columnas 
Resultado=np.zeros((Fl,Cl,Ch))
#Crea el kernel manualmente (Promedio y Gauss 5x5)

kernel_1 = np.array(([1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]),dtype='float')/25

kernel_2 = np.array(([-1,-1,-1],[-1,8,-1],[-1,-1,-1]),dtype='float')

Resultado = cv2.filter2D(Imagen,-1,kernel_1)

print('Imagen mejorada 1')
plt.imshow(Resultado.astype('uint8'),vmin=0, vmax=255) #Grafica la imagen
plt.show()
print('')


Resultado = cv2.filter2D(Resultado,-1,kernel_2)
#Muestra resultado
print('Imagen mejorada 2')
plt.imshow(Resultado.astype('uint8')*5,vmin=0, vmax=255) #Grafica la imagen
plt.show()
print('')
