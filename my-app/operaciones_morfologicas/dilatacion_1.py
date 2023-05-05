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
#Imagen=Imagen[:,:,[2,1,0]]#Organiza
Rojo=Imagen[:,:,2]
Verde=Imagen[:,:,1]
Azul=Imagen[:,:,0]
Gris=cv2.cvtColor(Imagen, cv2.COLOR_BGR2GRAY)

[Fl, Cl, Ch]=Imagen.shape
#Buscando fichas amarilla
Bin_Fichas_Amarillas =np.zeros((Fl,Cl))
Bin_Fichas_Amarillas = (Hue < 20)*(Hue > 10)*(Saturation > 130)
#Organizando resultado
Resultado_Fichas_Am = np.zeros((Fl,Cl,Ch))
Resultado_Fichas_Am[:,:,0]=Imagen[:,:,0]*Bin_Fichas_Amarillas
Resultado_Fichas_Am[:,:,1]=Imagen[:,:,1]*Bin_Fichas_Amarillas
Resultado_Fichas_Am[:,:,2]=Imagen[:,:,2]*Bin_Fichas_Amarillas
print('Imprimiendo resultado de segmentación')
fig2, (axs1,axs2,axs3) =plt.subplots(1, 3)
axs1.imshow(Imagen[:,:,[2,1,0]].astype('uint8'),vmin=0, vmax=255)
axs1.set_title('Original')
axs2.imshow(Bin_Fichas_Amarillas.astype('uint8'),vmin=0, vmax=1,cmap='gray')
axs2.set_title('Máscara')
axs3.imshow(Resultado_Fichas_Am[:,:,[2,1,0]].astype('uint8'),vmin=0, vmax=255)
axs3.set_title('Resultado')
plt.show()
print('')


###################   PROCESO PARA DILATACIÓN   ####################

#Se crea kernel de procesamiento
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(10,10))
dilated = cv2.dilate(Bin_Fichas_Amarillas.astype('uint8'),kernel)

#Armando resultado
Resultado_Fichas_Am2 = np.zeros((Fl,Cl,Ch))
Resultado_Fichas_Am2[:,:,0]=Imagen[:,:,0]*dilated
Resultado_Fichas_Am2[:,:,1]=Imagen[:,:,1]*dilated
Resultado_Fichas_Am2[:,:,2]=Imagen[:,:,2]*dilated

print('Imprimiendo resultado de dilatación')
fig2, (axs1,axs2,axs3,axs4) =plt.subplots(1, 4,figsize=(10,10))
axs1.imshow(Bin_Fichas_Amarillas.astype('uint8'),vmin=0, vmax=1,cmap='gray')
axs1.set_title('Máscara 1')
axs2.imshow(Resultado_Fichas_Am[:,:,[2,1,0]].astype('uint8'),vmin=0, vmax=255)
axs2.set_title('Resultado 1')
axs3.imshow(dilated.astype('uint8'),vmin=0, vmax=1,cmap='gray')
axs3.set_title('Máscara 2')
axs4.imshow(Resultado_Fichas_Am2[:,:,[2,1,0]].astype('uint8'),vmin=0, vmax=255)
axs4.set_title('Resultado 2')
plt.show()
print('')
