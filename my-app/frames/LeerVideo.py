#Algoritmo para detección de bordes
import cv2 # OpenCV para computer vision
import numpy as np # Para cálculo de matrices
import matplotlib.pyplot as plt #Para graficar

#Leyendo y mostrando video de referencia
Ruta = r'/home/felipeqg/Documents/Vision-Artificial/assets/videos/rhinos_1.avi'#Ubicación del video
Video = cv2.VideoCapture(Ruta) #Abre video o dispositivo de captura en una secuencia de imagenes
Contador = 0

while(Video.isOpened()):
    ret, frame = Video.read () ## ret devuelve un valor booleano
    if ret :
        Contador=Contador+1
        Color=frame[:,:,[2,1,0]]#Organiza
        print('')
        print('Fotograma número: ',Contador)
        plt.imshow(Color.astype('uint8'),vmin=0, vmax=255) # cmap='gray' Grafica la imagen 
        plt.show()    
    else:
        break
    
Video.release()
    