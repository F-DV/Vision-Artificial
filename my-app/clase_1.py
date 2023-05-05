#LEER IMAGEN CON OPENCV Y MOSTRARLA CON MATPLOTLIB

#Importando librerías
import cv2 # OpenCV para computer vision
import numpy as np # Para cálculo de matrices
import matplotlib.pyplot as plt #Para graficar

#Leyendo una imagen en grises
path = '/home/felipeqg/Documents/Vision-Artificial/assets/mandrill_colour.png'#Indica el direcorio de la imagen
Img = cv2.imread(path,0) #Lee la imagen en escala de grises
plt.imshow(Img,cmap='gray', vmin=0, vmax=255) #Grafica la imagen en campo de grises
plt.show