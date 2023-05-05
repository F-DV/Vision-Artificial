import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
import os #Habilita el manejo de directorios

Ruta2 = r'/home/felipeqg/Documents/Vision-Artificial/assets/images/Parcial_1_B.jpg'
Imagen2 = cv2.imread(Ruta2)
Imagen2=Imagen2[:,:,[2,1,0]]#Organiza imagen

kernel_1 = np.array(([-1,-1,-1],[-1,8,-1],[-1,-1,-1]),dtype='float')

Resultado = cv2.filter2D(Imagen2,-1,kernel_1)

print('Imagen Resultado_2')
plt.imshow(Resultado.astype('uint8'),vmin=0, vmax=255) #Grafica la imagen
plt.show()
print('')