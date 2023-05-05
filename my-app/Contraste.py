# AUMENTAR EL CONTRASTE DE UNA IMAGEN CON UN VALOR MEDIO
# HISTOGRAMA PARA ELEGIR EL VALOR DEL MEDIO

import cv2
import matplotlib.pyplot as plt
import numpy as np

nino = cv2.imread('/home/felipeqg/Documents/Vision-Artificial/assets/images/Parcial_1_C.jpg',0)

#Factor de aumento
K = 5

# obtengo la cantidad de filas y columnas que tiene la imagen
[ROWS,COLS] = nino.shape   
        
############## HISTOFGRAMA ################
#Lista llena de 0
histo = np.zeros(256)

#Recorro la imagen para leer los valores de colores
for row in range(0,ROWS):
    for col in range(0,COLS):
        
        histo[nino[row,col]] = histo[nino[row,col]] + 1

#Recorro el vecto para seleccionar el numero que mas se repite
posicion = 0
mayor = 0
for i in range(0,256):
    
    if(histo[i] > mayor):
        mayor = histo[i]
        posicion = i    
        
#Recorro la imagen
for row in range(0,ROWS):
    for col in range(0,COLS):
        
        #condicional para separar colores a partir del numero que mas se repite en el histograma
        if (nino[row,col] >= posicion):
            nino[row,col] = nino[row,col] + K
        else:
            nino[row,col] = nino[row,col] - K

        if (nino[row,col] >= 255):
            nino[row,col] = 255
        elif(nino[row,col] <= 0):
            nino[row,col] = 0
        else:
            nino[row,col] = nino[row,col]
                
plt.imshow(nino,cmap='gray')
plt.show()

