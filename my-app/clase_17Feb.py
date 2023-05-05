# CONTAR ARROZ EN UNA IMAGEN

#Importando librerías
import cv2 # OpenCV para computer vision
import numpy as np # Para cálculo de matrices
import matplotlib.pyplot as plt #Para graficar

#lee la imagen
img = cv2.imread('/home/felipeqg/Documents/Vision-Artificial/assets/images/Parcial_1_A.jpg',0)

cv2.imshow('Imagen',img); #grafica imagen con libreria cv2

#Espera entrada de teclado para cerrar la imagen
#cv2.waitKey(0)  
#cv2.destroyAllWindows()

####################
#Mostrar imagen del carro

Img2 = cv2.imread('/home/felipeqg/Documents/Vision-Artificial/assets/images/Parcial_1_A.jpg')

#Grafico con matplotlib
#plt.imshow(Img2,vmin=0, vmax=255) #Grafica la imagen en campo de grises
#plt.show

# 1)Forma Cambiamos manualmente los canales de BGR a RGB
Img3 =Img2[:,:,[2,1,0]]

# 2)Forma Cambia los canales con una funcion de openCV
#Img4 = cv2.cvtColor(Img2_raw, cv2.COLOR_BGR2RGB

#plt.imshow(Img3,vmin=0, vmax=255) 
#plt.show

#Imprimiendo el tamaño de la imagen
#[R, C, CH] = Img2.shape
#print(R)
#print(C)
#print(CH)

# otra forma de  imprimir dimensiones de la matriz anterior
#print('Las dimensiones de la imagen son:',Img2.shape)
#Dejando un espacioo en blanco
#print('')
# Imprimeindo un pixel de la imagen
#print('La intensidad del pixel es:', Img2[350,350])

##################################################3
# EJERCICIO CONTAR ARROZ EN UNA IMAGEN

# Leo la imagen
riceImage = cv2.imread('/home/felipeqg/Documents/Vision-Artificial/assets/images/Parcial_1_A.jpg',0)

# Hago una copia de la imagen para modificarla
copyRiceImage = riceImage

# Tamaño de la imagen en filas y columnas
[ROWS,COLS] = riceImage.shape
print(ROWS,COLS);

# Inicializo los pixeles Negros y blancos
white = 0
black = 0

#Recorro la matriz de la imagen
for fila in range(0,ROWS):
    for columna in range(0,COLS):
        if (riceImage[fila,columna]>122):
            white = white + 1
            
            #Cambio el color del pixel actual a blanco
            copyRiceImage[fila,columna] = 255
        else:
            black = black + 1
            #Cambio el color del pixel actual a negro
            copyRiceImage[fila,columna] = 0
            
# imprimo el resultado de pixeles encontrados
print('Los pixeles negros son: ', black)
print('los pixeles blancos son: ',white)
print('el total de pixeles en la imagen es: ', ROWS*COLS)
print('La sumatoria de mis pixeles es: ', black+white)


# Imprimo la imagen
plt.imshow(copyRiceImage,cmap='gray',vmin=0, vmax=255)
plt.show