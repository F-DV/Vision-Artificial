#Cargando librerías
import cv2 # OpenCV para computer vision
import numpy as np # Para cálculo de matrices
import matplotlib.pyplot as plt #Para graficar
import os #Habilita el manejo de directorios

#Leyendo imagen de entrada
Ruta = r'/home/felipeqg/Documents/Vision-Artificial/assets/images/fichas.png' #Ubicación de la imagen desde el google drive
Imagen = cv2.imread(Ruta)#Lee

print('Mostrando imagen de entrada')
plt.imshow(Imagen[:,:,[2,1,0]].astype('uint8'),vmin=0, vmax=255) #Muestra
plt.show()
print('')

#Extracción de canales en HSV
Imagen_hsv = cv2.cvtColor(Imagen,cv2.COLOR_BGR2HSV)
Hue=Imagen_hsv[:,:,0]
Saturation=Imagen_hsv[:,:,1]
Value=Imagen_hsv[:,:,2]

#Extracción de canales en RGB
Imagen=Imagen[:,:,[2,1,0]]#Organiza
Rojo=Imagen[:,:,0]
Verde=Imagen[:,:,1]
Azul=Imagen[:,:,2]
Gris=cv2.cvtColor(Imagen, cv2.COLOR_BGR2GRAY)

#Segmentar fichas verdes
Bin_Fichas_Verdes = (Hue > 60)*(Hue < 120)*(Value < 90)*(Rojo < 70)

#Organizando resultado
[Fl, Cl, Ch]=Imagen.shape
Resultado_Fichas_V = np.zeros((Fl,Cl,Ch))
Resultado_Fichas_V[:,:,0]=Imagen[:,:,0]*Bin_Fichas_Verdes
Resultado_Fichas_V[:,:,1]=Imagen[:,:,1]*Bin_Fichas_Verdes
Resultado_Fichas_V[:,:,2]=Imagen[:,:,2]*Bin_Fichas_Verdes

print('Imprimiendo resultado de segmentación')
fig2, (axs1,axs2,axs3) =plt.subplots(1, 3,figsize=(8,8))
axs1.imshow(Imagen.astype('uint8'),vmin=0, vmax=255)
axs1.set_title('Original')
axs2.imshow(Bin_Fichas_Verdes.astype('uint8'),vmin=0, vmax=1,cmap='gray')
axs2.set_title('Máscara')
axs3.imshow(Resultado_Fichas_V.astype('uint8'),vmin=0, vmax=255)
axs3.set_title('Resultado')
plt.show()
print('')