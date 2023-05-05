#SUMAR DOS IMAGENES 

import cv2
import matplotlib.pyplot as plt
import numpy as np

#Leer imagenes
img1 = cv2.imread('/home/felipeqg/Documents/Vision-Artificial/assets/Lena.png')
img2 = cv2.imread('/home/felipeqg/Documents/Vision-Artificial/assets/car.jpg')

#Organizar imagenes en RGB
imgLena = img1[:,:,[2,1,0]] 
imgCar = img2[:,:,[2,1,0]] 

#Cortamos imagenes al mismo tamaño
cutLena = imgLena[140:400, 140:400,:]
cutCar = imgCar[140:400, 140:400,:]



[ROWS,COLS,CH] = cutLena.shape

#Creamos matriz vacia
res = np.zeros([ROWS,COLS,CH])

for row in range(0,ROWS):
    for col in range(0,COLS):
        for ch in range(0,CH):
            res[row,col,ch] = np.array(cutLena[row,col,ch]) + np.array(cutCar[row,col,ch])
            
            
# Imprimimos el resultado 
plt.imshow(res.astype('uint8'), vmin=0,vmax=255)
plt.show()