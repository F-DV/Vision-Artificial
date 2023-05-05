# APRENDER A RECORTAR IMAGENES Y 
# AUMENTAR O DISMINUIR BRILLO

#importando librerias
import cv2
import matplotlib.pyplot as plt
import numpy as np 

#Lee+ la imagen
img = cv2.imread('/home/felipeqg/Documents/Vision-Artificial/assets/Lena.png')

#Organizamos los canales 
imgLena = img[:,:,[2,1,0]]


#Realizamos un recorde de la imagen
cutImage = imgLena[200:319, 200:309,:]

#imprimir recorte
#plt.imshow(cutImage, vmax=255, vmin=0)
#plt.show()

##AUMENTAR INTENSIDAD DEL BRILLO
#obtenemos las filas, columnas y canales de la imagen
[ROWS,COLS,CH] = img.shape

#Convierte la matriz en ceros
res = np.zeros([ROWS,COLS,CH])

#Recorremos matriz para aumentar o disminuir brillo
for row in range(0,ROWS):
    for col in range(0,COLS):
        for ch in range(0,CH):
            res[row,col,ch] = imgLena[row,col,ch] + 150;
            if (res[row,col,ch] >= 255):
                res[row,col,ch] = 255
            else:
                res[row,col,ch] = res[row,col,ch]

# Imprimimos el resultado del brillo con un tipo
plt.imshow(res.astype('uint8'), vmin=0,vmax=255)
plt.show()