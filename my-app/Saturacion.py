# CAMBIAR SISTEMA DE COLORES PARA REGULAR LA SATURACION DE UNA IMAGEN

import cv2
import matplotlib.pyplot as plt
import numpy as np
#H L S (HUE SATURARION INTENSITY)

lena = cv2.imread('/home/felipeqg/Documents/Vision-Artificial/assets/images/Parcial_1_A.jpg')

lena_HLS = cv2.cvtColor(lena,cv2.COLOR_BGR2HLS)

[R,C,CH] =  lena_HLS.shape

ch_H = 0;
ch_S = 1;
ch_L = 2;

value_H = 90
value_L = 90
value_S = 90

#Recorre H
for y in range(0,R):
    for x in range(0,C):
        lena_HLS[y,x,ch_H] = lena_HLS[y,x,ch_H] + value_H
    
#Recorre S    
for y in range(0,R):
    for x in range(0,C):
        lena_HLS[y,x,ch_L] =lena_HLS[y,x,ch_L] +  value_L

#Recorre V        
for y in range(0,R):
    for x in range(0,C):
        lena_HLS[y,x,ch_S] =lena_HLS[y,x,ch_S] + value_S 
   
lena_RGB = cv2.cvtColor(lena_HLS,cv2.COLOR_HLS2RGB)

plt.axis("off")
plt.imshow(lena_RGB, vmax=255,vmin=0)
plt.show()
