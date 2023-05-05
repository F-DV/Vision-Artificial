import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
import os #Habilita el manejo de directorios

#Leyendo y mostrando imagen  con ruido
Ruta1 = r'/home/felipeqg/Documents/Vision-Artificial/assets/images/Parcial_1_A.jpg'#Ubicación de la imagen desde el google drive
Ruta2 = r'/home/felipeqg/Documents/Vision-Artificial/assets/images/Parcial_1_B.jpg'#Path Parcial_1_B.jpg
Ruta3 = r'/home/felipeqg/Documents/Vision-Artificial/assets/images/Parcial_1_C.jpg'#Path Parcial_1_C.jpg
Ruta4 = r'/home/felipeqg/Documents/Vision-Artificial/assets/images/messi.png' # Path de imagen de Messi

Imagen1 = cv2.imread(Ruta1)#Lee imagen Parcial_1_A.jpg
Imagen2 = cv2.imread(Ruta2)#Lee imagen Parcial_1_B.jpg
Imagen3 = cv2.imread(Ruta3)#Lee imagen Parcial_1_C.jpg
Imagen4 = cv2.imread(Ruta4)#Lee imagen de Messi

Imagen1=Imagen1[:,:,[2,1,0]]#Organiza imagen
Imagen2=Imagen2[:,:,[2,1,0]]
Imagen3=Imagen3[:,:,[2,1,0]]#Organiza imagen
Imagen4=Imagen4[:,:,[2,1,0]]#Organiza imagen


#=============================================================================
[ROWS,COLS,CH] = Imagen1.shape
[ROW2,COLS2,CH2] = Imagen2.shape
[ROW3,COLS3,CH3] = Imagen3.shape
#[ROWS4,COLS4,CH4] = Imagen4.shape


############### IMAGEN Parcial_1_A.jpg ##################################
print('Imagen Parcial_1_A  Original')
plt.imshow(Imagen1.astype('uint8'),vmin=0, vmax=255) #Muestra
plt.show()
print('')

#Variables
contraste = 30
brillo = 80


######################### BRILLO ###########################
#Convierte la matriz en ceros
res1 = np.zeros([ROWS,COLS,CH])

#Recorremos matriz para aumentar o disminuir brillo
for row in range(0,ROWS):
    for col in range(0,COLS):
        for ch in range(0,CH):
            if (row >= 160 and row <= 300):
                if(col >=175 and col<= 420): 
                         
                    res1[row,col,ch] = Imagen1[row,col,ch] + brillo;
                    if (res1[row,col,ch] >= 255):
                        res1[row,col,ch] = 255
                    else:
                        res1[row,col,ch] = res1[row,col,ch]
                else:
                    res1[row,col,ch] = Imagen1[row,col,ch]
            else:
                res1[row,col,ch] = Imagen1[row,col,ch]

#Muestra resultado Resultado_1.bmp
print('Imagen Parcial_1_A Modificada')
plt.imshow(res1.astype('uint8'),vmin=0, vmax=255)#Grafica la imagen
plt.figure(figsize=(20,20))
plt.show()
print('')


#################### IMAGEN Parcial_1_B.jpg #####################
print('Imagen Parcial_1_B  Original')
plt.imshow(Imagen2.astype('uint8'),vmin=0, vmax=255) #Muestra
plt.show()
print('')
Imagen2= cv2.cvtColor(Imagen2,cv2.COLOR_RGB2HLS)

# Variables para saturacion y brillo
value_Brillo = 40
value_H = 89
value_L = 50
value_S = 5

#=============== saturacion ================
#Canales
ch_H = 0;
ch_S = 1;
ch_L = 2;
#Recorre H
for y in range(0,ROW2):
    for x in range(0,COLS2):
        Imagen2[y,x,ch_H] = Imagen2[y,x,ch_H] + value_H
    
#Recorre L
for y in range(0,ROW2):
    for x in range(0,COLS2):
        Imagen2[y,x,ch_L] =Imagen2[y,x,ch_L] +  value_L

#Recorre S        
for y in range(0,ROW2):
    for x in range(0,COLS2):
        Imagen2[y,x,ch_S] =Imagen2[y,x,ch_S] + value_S 

#Pasamos a RGB    
Imagen2_RGB = cv2.cvtColor(Imagen2,cv2.COLOR_HLS2BGR) 

#============== Brillo ==================

res = np.zeros([ROWS,COLS,CH])

#Recorremos matriz para aumentar o disminuir brillo
for row in range(0,ROW2):
    for col in range(0,COLS2):
        for ch in range(0,CH2):
            res[row,col,ch] = Imagen2_RGB[row,col,ch] + value_Brillo;
            if (res[row,col,ch] >= 255):
                res[row,col,ch] = 255
            else:
                res[row,col,ch] = res[row,col,ch]
            
print('Imagen Parcial_1_B Modificada')
plt.imshow(res.astype('uint8'),vmin=0, vmax=255) #Grafica la imagen
plt.show()
print('')

#################### IMAGEN Parcial_1_C.jpg #####################

print('Imagen Parcial_1_C  Original')
plt.imshow(Imagen3.astype('uint8'),vmin=0, vmax=255) #Muestra
plt.show()
print('')

############# SELECIONAR ZONA A ILUMINAR ########
"""Se ilumina esa area ya que hay un automovil estacionado
    que no se logra ver en la imagen original
"""
Imagen3HLS = cv2.cvtColor(Imagen3,cv2.COLOR_BGR2HLS)    

#Algoritmo para Iluminar la imagen
chH = 0;
chS = 1;
chL = 2;

valueH = -1
valueL = 5
valueS = 5

#Recorre H
for y in range(0,ROW3):
    for x in range(0,COLS3):
        Imagen3HLS[y,x,chH] = Imagen3HLS[y,x,chH] + valueH
    
#Recorre S    
for y in range(0,ROW3):
    for x in range(0,COLS3):
        Imagen3HLS[y,x,chL] =Imagen3HLS[y,x,chL] +  valueL

#Recorre V        
for y in range(0,ROW3):
    for x in range(0,COLS3):
        Imagen3HLS[y,x,chS] =Imagen3HLS[y,x,chS] + valueS 
   
#Convierto denuevo la imagen a RGB    
Imagen3_RGB = cv2.cvtColor(Imagen3HLS,cv2.COLOR_HLS2RGB)


#Convierte la matriz en ceros
res2 = np.zeros([ROW3,COLS3,CH3])

#Recorremos matriz de la imagen
for row in range(0,ROW3):
    for col in range(0,COLS3):
        for ch in range(0,CH3):
            if (row >= 290 and row <= 500):
                if(col >=60 and col<= 500):    
                    res2[row,col,ch] = Imagen3_RGB[row,col,ch] + 15;
                else:
                    res2[row,col,ch] = Imagen3[row,col,ch]
            else:
                res2[row,col,ch] = Imagen3[row,col,ch]



print('Imagen Parcial_1_C  Modificada')
plt.imshow(res2.astype('uint8'),vmin=0, vmax=255) #Muestra
plt.show()
print('')

############## IMAGEN DETECCION DE BORDES DE MESSI ###############
print('Messi Original')
plt.imshow(Imagen4.astype('uint8'),vmin=0, vmax=255,cmap='gray') #Grafica la imagen
plt.figure(figsize=(20,20))
plt.show()
print('')

""" 
Filtramos la imagen de Messi con el filtro
medianBlur para quitarle el ruido ya que fue el mas efectivo, luego pasamos la imagen
resultande a grises para aplicarvla funcion de opencv Sobel para detectar bordes

"""

messiFiltrado = cv2.medianBlur(Imagen4,9) #Filtro medianBlur
messiGris = cv2.cvtColor(messiFiltrado,cv2.COLOR_BGR2GRAY)# Imagen a grises

sobelX = cv2.Sobel(messiGris, cv2.CV_64F,1,0)
sobelY = cv2.Sobel(messiGris, cv2.CV_64F,0,1)
sobelx = np.uint8(np.absolute(sobelX))
sobely = np.uint8(np.absolute(sobelY))

sobelTotal = cv2.bitwise_or(sobelx,sobely)

print('Bordes de Messi')
plt.imshow(sobelTotal.astype('uint8'),vmin=0, vmax=255,cmap='gray') #Grafica la imagen
plt.figure(figsize=(20,20))
plt.show()
print('')