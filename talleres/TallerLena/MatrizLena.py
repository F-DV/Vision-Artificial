import cv2#Solo para leer la imagen
import matplotlib.pyplot as plt
import numpy as np

#Leo imagen con cv2
img = cv2.imread('/home/felipeqg/Documents/Vision-Artificial/TallerLena/Lenna.png')

#Cambio los canales de posicion
lena = cv2.cvtColor(img,cv2.COLOR_BGR2RGB);
lenaCut = lena[0:439,0:439]
# asigno las filas y columnas que tiene la imagen en en variables
[ROWS,COLS,CH] = lenaCut.shape

lenaMinus_90 = np.zeros([COLS,ROWS,CH])#cambio de filas por columnas
lenaPlus_90 = np.zeros([COLS,ROWS,CH])#cambio de filas por columnas||
lenaFlipV = np.zeros([ROWS,COLS,CH]) #mismas filas y columnas de la imagen original
lenaFlipH = np.zeros([ROWS,COLS,CH]) #mismas filas y columnas de la imagen original
lenaArray_A = np.zeros([ROWS,COLS,CH])
lenaArray_B = np.zeros([ROWS,COLS,CH])

#Recorremos la imagen orinial y vamos asigando el valor en la posicion que queremos de la imagen modificada

#lena minus 90
for row in range(0,ROWS):
    colEnd = COLS
    for col in range(0,COLS):
        colEnd = colEnd - 1
        lenaMinus_90[colEnd,row] = lena[row,col] 

#lena plus 90
for col in range(0,COLS):
    rowEnd = ROWS
    for row in range(0,ROWS):
        rowEnd = rowEnd - 1
        lenaPlus_90[col,rowEnd] = lena[row,col] 

#lena flip V
for row in range(0,ROWS):
    colEnd = COLS 
    for col in range(0,COLS):
        colEnd= colEnd -1
        lenaFlipV[row,colEnd] = lena[row,col] 
               
#lena flip H
for col in range(0,COLS):
    rowEnd = ROWS 
    for row in range(0,ROWS):
        rowEnd= rowEnd - 1
        lenaFlipH[rowEnd,col] = lena[row,col] 

#lena ARRAY A 
for row in range(0,ROWS):
    for col in range(0,COLS):
        if(row > (ROWS/2)):
            lenaArray_A[row,col] = lenaFlipV[row,col]
        else:    
            lenaArray_A[row,col] = lenaFlipH[row+219,col]
                      
#lena ARRAY B        
for row in range(0,ROWS):
    for col in range(0,COLS):
        if(row > (ROWS/2)):
            if(col < (COLS/2)):    
            #inferior izquierda
                lenaArray_B[row,col] = lenaMinus_90[row,col+219]
            else:
            #inferior derecha
                lenaArray_B[row,col] = lenaPlus_90[row,col-219]            
        elif(row < (ROWS/2)):            
            if(col < (COLS/2)):
                #superior izquierda
                lenaArray_B[row,col] = lenaPlus_90[row,col+219]
            else:
                #superior derecha
                lenaArray_B[row,col] = lenaMinus_90[row,col-219]

#Se grafica todas la imagenes modificadas
fig = plt.figure(figsize=(10, 7)) #Se define el tamaño para mostrar las 6 imagenes

fig.add_subplot(2,3,1)
plt.axis("off")
plt.imshow(lenaPlus_90.astype('uint8'), vmin=0,vmax=255)
plt.title("LenaPlus_90")

fig.add_subplot(2,3,2)
plt.axis("off")
plt.imshow(lenaMinus_90.astype('uint8'), vmin=0,vmax=255)
plt.title("LenaMinus_90")

fig.add_subplot(2,3,3)
plt.axis("off")
plt.imshow(lenaFlipH.astype('uint8'), vmin=0,vmax=255)
plt.title("LenaFlip_H")

fig.add_subplot(2,3,4)
plt.axis("off")
plt.imshow(lenaFlipV.astype('uint8'), vmin=0,vmax=255)
plt.title("LenaFlip_V")

fig.add_subplot(2,3,5)
plt.axis("off")
plt.imshow(lenaArray_A.astype('uint8'), vmin=0,vmax=255)
plt.title("LenaArray_A")

fig.add_subplot(2,3,6)
plt.axis("off")
plt.imshow(lenaArray_B.astype('uint8'), vmin=0,vmax=255)
plt.title("LenaArray_B")