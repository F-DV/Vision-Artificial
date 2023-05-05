#Cargando librerías
import cv2 # OpenCV para computer vision
import numpy as np # Para cálculo de matrices
import matplotlib.pyplot as plt #Para graficar
import os #Habilita el manejo de directorios

#Leyendo imagen de entrada
Ruta = r'/home/felipeqg/Documents/Vision-Artificial/assets/images/rubik.png' #Ubicación de la imagen desde el google drive
Imagen = cv2.imread(Ruta)#Lee
Imagen=Imagen[:,:,[2,1,0]]#Organiza

"""
print('Mostrando imagen de entrada')
plt.imshow(Imagen.astype('uint8'),vmin=0, vmax=255) #Muestra
plt.show()
print('')
"""

#Extracción de canales en HSV
Imagen=Imagen[:,:,[2,1,0]]
Imagen_hsv = cv2.cvtColor(Imagen,cv2.COLOR_BGR2HSV)
Hue=Imagen_hsv[:,:,0]
Saturation=Imagen_hsv[:,:,1]
Value=Imagen_hsv[:,:,2]

#Extracción de canales en RGB
#Imagen=Imagen[:,:,[2,1,0]]#Organiza
Rojo=Imagen[:,:,2]
Verde=Imagen[:,:,1]
Azul=Imagen[:,:,0]
Gris=cv2.cvtColor(Imagen, cv2.COLOR_BGR2GRAY)

#Busqueda del valor apuntuando a los pixeles de interes 

#Azul[55:65,400:410] = 255
#print("Valor del color del pixel: ", Gris[190:195,550:555])
#print("Valor del color del pixel: ", Gris[55:65,400:410])
#plt.imshow(Azul.astype('uint8'),vmin=0, vmax=255, cmap='gray')


#===================== SEGMENTACION ================
#Segmentando el rojo
[Fl, Cl, Ch]=Imagen.shape
Bin_Fichas_Rojas =np.zeros((Fl,Cl))
Bin_Fichas_Rojas = (Hue<3)*(Verde < 180)
#(Hue > 170)*(Hue < 180)*(Saturation > 130)

#Organizando resultado
Resultado_Fichas_R = np.zeros((Fl,Cl,Ch))
Resultado_Fichas_R[:,:,0]=Imagen[:,:,0]*Bin_Fichas_Rojas
Resultado_Fichas_R[:,:,1]=Imagen[:,:,1]*Bin_Fichas_Rojas
Resultado_Fichas_R[:,:,2]=Imagen[:,:,2]*Bin_Fichas_Rojas
print("Rojo")
plt.imshow(Resultado_Fichas_R[:,:,[2,1,0]].astype('uint8'),vmin=0, vmax=255)
plt.show()


#Segmentando fichas verde
[Fl, Cl, Ch]=Imagen.shape
Bin_Fichas_Verdes =np.zeros((Fl,Cl))
Bin_Fichas_Verdes = (Hue > 65)*(Hue < 85)*(Rojo < 92)
#Organizando resultado
Resultado_Fichas_V = np.zeros((Fl,Cl,Ch))
Resultado_Fichas_V[:,:,0]=Imagen[:,:,0]*Bin_Fichas_Verdes
Resultado_Fichas_V[:,:,1]=Imagen[:,:,1]*Bin_Fichas_Verdes
Resultado_Fichas_V[:,:,2]=Imagen[:,:,2]*Bin_Fichas_Verdes
print("Verde")
plt.imshow(Resultado_Fichas_V[:,:,[2,1,0]].astype('uint8'),vmin=0, vmax=255)
plt.show()

#Segmentando el Morado
Bin_Fichas_Morado =np.zeros((Fl,Cl))
Bin_Fichas_Morado = (Azul > 175)*(Azul < 245)*(Rojo < 110)
#Organizando resultado
Resultado_Fichas_M = np.zeros((Fl,Cl,Ch))
Resultado_Fichas_M[:,:,0]=Imagen[:,:,0]*Bin_Fichas_Morado
Resultado_Fichas_M[:,:,1]=Imagen[:,:,1]*Bin_Fichas_Morado
Resultado_Fichas_M[:,:,2]=Imagen[:,:,2]*Bin_Fichas_Morado
print("Morado")
plt.imshow(Resultado_Fichas_M[:,:,[2,1,0]].astype('uint8'),vmin=0, vmax=255)
plt.show()

#Segmentando el Amarillo
Bin_Fichas_Amarillo =np.zeros((Fl,Cl))
Bin_Fichas_Amarillo =(Hue>29)*(Hue<31)*(Azul<105)
#Organizando resultado
Resultado_Fichas_A = np.zeros((Fl,Cl,Ch))
Resultado_Fichas_A[:,:,0]=Imagen[:,:,0]*Bin_Fichas_Amarillo
Resultado_Fichas_A[:,:,1]=Imagen[:,:,1]*Bin_Fichas_Amarillo
Resultado_Fichas_A[:,:,2]=Imagen[:,:,2]*Bin_Fichas_Amarillo
print("Amarillo")
plt.imshow(Resultado_Fichas_A[:,:,[2,1,0]].astype('uint8'),vmin=0, vmax=255)
plt.show()

#Segmentando el Naranja
Bin_Fichas_Naranja = np.zeros((Fl,Cl))
Bin_Fichas_Naranja =(Hue>5)*(Hue<15)
#Organizando resultado
Resultado_Fichas_N = np.zeros((Fl,Cl,Ch))
Resultado_Fichas_N[:,:,0]=Imagen[:,:,0]*Bin_Fichas_Naranja
Resultado_Fichas_N[:,:,1]=Imagen[:,:,1]*Bin_Fichas_Naranja
Resultado_Fichas_N[:,:,2]=Imagen[:,:,2]*Bin_Fichas_Naranja
print("Naranja")
plt.imshow(Resultado_Fichas_N[:,:,[2,1,0]].astype('uint8'),vmin=0, vmax=255)
plt.show()

#Segmentando el Blanco
Bin_Fichas_Blanco = np.zeros((Fl,Cl))
Bin_Fichas_Blanco =(Saturation < 5)
#Organizando resultado
Resultado_Fichas_B = np.zeros((Fl,Cl,Ch))
Resultado_Fichas_B[:,:,0]=Imagen[:,:,0]*Bin_Fichas_Blanco
Resultado_Fichas_B[:,:,1]=Imagen[:,:,1]*Bin_Fichas_Blanco
Resultado_Fichas_B[:,:,2]=Imagen[:,:,2]*Bin_Fichas_Blanco
print("Blanco")
plt.imshow(Resultado_Fichas_B[:,:,[2,1,0]].astype('uint8'),vmin=0, vmax=255)
plt.show()



#======== SEGMENTACION DE CELULAS 1_OR.PNG=========
Ruta_1 = r'/home/felipeqg/Documents/Vision-Artificial/assets/images/1_OR.png'
Imagen_celulas1 = cv2.imread(Ruta_1)#Lee
Ruta_2 = r'/home/felipeqg/Documents/Vision-Artificial/assets/images/1_GT.png'
Imagen_GT =cv2.imread(Ruta_2)

#Extracción de canales en HSV
Imagen_Celulas_hsv = cv2.cvtColor(Imagen_celulas1,cv2.COLOR_BGR2HSV)
Hue=Imagen_Celulas_hsv[:,:,0]
Saturation=Imagen_Celulas_hsv[:,:,1]
Value=Imagen_Celulas_hsv[:,:,2]

#Extracción de canales en RGB
Rojo=Imagen_celulas1[:,:,2]
Verde=Imagen_celulas1[:,:,1]
Azul=Imagen_celulas1[:,:,0]
Gris=cv2.cvtColor(Imagen_celulas1, cv2.COLOR_BGR2GRAY)

[ROWS,COLS,CHS] = Imagen_celulas1.shape

Resultado_Binario_1 = np.zeros((ROWS,COLS))
Matriz_confusion = np.zeros((2,2))

#Segmentando las celular en 1_OR.png
[Fl, Cl, Ch]= Imagen_celulas1.shape

Bin_violeta = np.zeros((Fl,Cl))
Bin_Violeta =(Hue > 110)*(Hue < 117)+(Rojo < 140)

#Organizando resultado
Prediccion_1 = np.zeros((Fl,Cl,Ch))
Prediccion_1[:,:,0]=Imagen_celulas1[:,:,0]*Bin_Violeta
Prediccion_1[:,:,1]=Imagen_celulas1[:,:,1]*Bin_Violeta
Prediccion_1[:,:,2]=Imagen_celulas1[:,:,2]*Bin_Violeta

#print("Celulas")
#plt.imshow(Prediccion_1[:,:,[2,1,0]].astype('uint8'),vmin=0, vmax=255)
#plt.show()

#Binarizamos imagen
for row in range(0,Fl):
    for col in range(0,Cl):
        for ch in range(0,Ch):
            if(Prediccion_1[row,col,ch] > 50):
                Prediccion_1[row,col] = 255
            else:
                Prediccion_1[row,col] = 0 

print("Resultado")
plt.imshow(Prediccion_1.astype('uint8'),vmin=0, vmax=255)
plt.show()


for row in range(0,ROWS):
    for col in range(0,COLS):
        if((Prediccion_1[row,col] - Imagen_GT[row,col]==255) == 0).all():
            #Verdaderos Positivos
            Matriz_confusion[0,0] = Matriz_confusion[0,0] + 1 
        elif(((Prediccion_1[row,col] - Imagen_GT[row,col]==0) == 0)).all():
            #Verdaderos Negativos
            Matriz_confusion[1,1] = Matriz_confusion[1,1] + 1
        elif(((Prediccion_1[row,col] - Imagen_GT[row,col]==255) < 0).all()):
            # Falsos Negativos
            Matriz_confusion[1,0] = Matriz_confusion[1,0] + 1
        elif(((Prediccion_1[row,col] - Imagen_GT[row,col] == 0) > 0)).all():
            #Falsos Positivos
            Matriz_confusion[0,1] = Matriz_confusion[0,1] + 1

print("Matriz de Confusion: ", Matriz_confusion)


#======== SEGMENTACION DE CELULAS 2_OR.PNG=========
Ruta_3 = r'/home/felipeqg/Documents/Vision-Artificial/assets/images/2_OR.png'
Imagen_celulas2 = cv2.imread(Ruta_3)#Lee
Ruta_4 = r'/home/felipeqg/Documents/Vision-Artificial/assets/images/2_GT.png'
Imagen_GT_2 =cv2.imread(Ruta_4)

#Extracción de canales en HSV
Imagen_Celulas_hsv2 = cv2.cvtColor(Imagen_celulas2,cv2.COLOR_BGR2HSV)
Hue2=Imagen_Celulas_hsv2[:,:,0]
Saturation2=Imagen_Celulas_hsv2[:,:,1]
Value2=Imagen_Celulas_hsv2[:,:,2]

#Extracción de canales en RGB
Rojo2=Imagen_celulas2[:,:,2]
Verde2=Imagen_celulas2[:,:,1]
Azul2=Imagen_celulas2[:,:,0]
Gris2=cv2.cvtColor(Imagen_celulas2, cv2.COLOR_BGR2GRAY)

[ROWS2,COLS2,CHS2] = Imagen_celulas2.shape

Resultado_Binario_2 = np.zeros((ROWS2,COLS2))
Matriz_confusion2 = np.zeros((2,2))

#Segmentando las celular en 2_OR.png
[Fl2, Cl2, Ch2]= Imagen_celulas2.shape

Bin_cel = np.zeros((Fl,Cl))
Bin_cel =(Hue2 > 110)*(Hue2 < 117)+(Rojo2 < 140)

#Organizando resultado
Prediccion_2 = np.zeros((Fl2,Cl2,Ch2))
Prediccion_2[:,:,0]=Imagen_celulas2[:,:,0]*Bin_cel
Prediccion_2[:,:,1]=Imagen_celulas2[:,:,1]*Bin_cel
Prediccion_2[:,:,2]=Imagen_celulas2[:,:,2]*Bin_cel

#print("Celulas 2")
#plt.imshow(Prediccion_2[:,:,[2,1,0]].astype('uint8'),vmin=0, vmax=255)
#plt.show()

#Binarizamos imagen
for row in range(0,Fl2):
    for col in range(0,Cl2):
        for ch in range(0,Ch2):
            if(Prediccion_2[row,col,ch] > 50):
                Prediccion_2[row,col] = 255
            else:
                Prediccion_2[row,col] = 0 

print("Resultado 2")
plt.imshow(Prediccion_2.astype('uint8'),vmin=0, vmax=255)
plt.show()


for row in range(0,ROWS2):
    for col in range(0,COLS2):
        if((Prediccion_2[row,col] - Imagen_GT_2[row,col]==255) == 0).all():
            #Verdaderos Positivos
            Matriz_confusion2[0,0] = Matriz_confusion2[0,0] + 1 
        elif(((Prediccion_2[row,col] - Imagen_GT_2[row,col]==0) == 0)).all():
            #Verdaderos Negativos
            Matriz_confusion2[1,1] = Matriz_confusion2[1,1] + 1
        elif(((Prediccion_2[row,col] - Imagen_GT_2[row,col]==255) < 0).all()):
            # Falsos Negativos
            Matriz_confusion2[1,0] = Matriz_confusion2[1,0] + 1
        elif(((Prediccion_2[row,col] - Imagen_GT_2[row,col] == 0) > 0)).all():
            #Falsos Positivos
            Matriz_confusion2[0,1] = Matriz_confusion2[0,1] + 1

print("Matriz de Confusion 2: ", Matriz_confusion2)


