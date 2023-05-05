#Algoritmo para filtrado prromedio según número de vecinos
import cv2 # OpenCV para computer vision
import numpy as np # Para cálculo de matrices
import matplotlib.pyplot as plt #Para graficar
import os #Habilita el manejo de directorios

#Leyendo y mostranso imagen  con ruido
Ruta = r'/home/felipeqg/Documents/Vision-Artificial/assets/images/Parcial_1_B.jpg'#Ubicación de la imagen desde el google drive
Imagen = cv2.imread(Ruta)#Lee
Imagen=Imagen[:,:,[2,1,0]]#Organiza
print('Mostrando imagen con ruido')
plt.imshow(Imagen.astype('uint8'),vmin=0, vmax=255)
plt.figure(figsize=(20,20))
plt.show()
print('')

#=============================================================================
#Mejorando problemas de ruido 
[Fl, Cl, Ch]=Imagen.shape #Genera dos variables para almacenar el número de filas y Columnas 
Resultado=np.zeros((Fl,Cl,Ch))
#Crea el kernel
kernel = np.ones((7,7),np.float32)/49
#Filtra la imagen utilizando el kernel anterior
Resultado = cv2.filter2D(Imagen,-1,kernel)
#Muestra resultado
print('Imagen mejorada')
plt.imshow(Resultado.astype('uint8'),vmin=0, vmax=255)#Grafica la imagen
plt.figure(figsize=(20,20))
plt.show()
print('')