#Cargando librerías
import cv2 # OpenCV para computer vision
import numpy as np # Para cálculo de matrices
import matplotlib.pyplot as plt #Para graficar

RutaImagenBordes = r'/home/felipeqg/Documents/Vision-Artificial/assets/images/imagen_1.JPG' # Path de imagen 
Imagen_1 = cv2.imread(RutaImagenBordes)#Lee imagen 
Imagen_1=Imagen_1[:,:,[2,1,0]]#Organiza imagen

print('Imagen_1 Original')
plt.imshow(Imagen_1.astype('uint8'),vmin=0, vmax=255,cmap='gray') #Grafica la imagen
plt.figure(figsize=(20,20))
plt.show()
print('')
  
imagenFiltrada = cv2.medianBlur(Imagen_1,9) #Filtro 
imagenFiltrada2 = cv2.medianBlur(imagenFiltrada,9) #Filtro 
imagenFiltrada3 = cv2.medianBlur(imagenFiltrada2,9) #Filtro 
imagenFiltrada4 = cv2.medianBlur(imagenFiltrada3,9) #Filtro 

imagenGris = cv2.cvtColor(imagenFiltrada4,cv2.COLOR_BGR2GRAY)# Imagen a grises

sobelX = cv2.Sobel(imagenGris, cv2.CV_64F,1,0)
sobelY = cv2.Sobel(imagenGris, cv2.CV_64F,0,1)
sobelx = np.uint8(np.absolute(sobelX))
sobely = np.uint8(np.absolute(sobelY))

sobelTotal = cv2.bitwise_or(sobelx,sobely)

print('Bordes de Imagen_1')
plt.imshow(sobelTotal.astype('uint8'),vmin=0, vmax=255,cmap='gray') #Grafica la imagen
plt.figure(figsize=(20,20))
plt.show()
print('')