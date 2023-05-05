# Leer imagen a color y hacer 3 copias
# 1) A la primera imagen aumentar el canal Rojo
# 2) A la segunda imagen aumentar el canal  verde
# 3) A la tercera imagen aumentar el canar Azul

#Importamos librerias a utilzar
import cv2
import matplotlib.pyplot as plt

# Leemos la imagen
img = cv2.imread('/home/felipeqg/Documents/Vision-Artificial/assets/mandrill_colour.png')

#Organizamos los canales en una nueva copia
imgR = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

print('La forma de la imagen es: ', img.shape)


[ROWS,COLS,CH] = img.shape

# Recorro la matriz de la imagen y aumento la intensidad del canal
for row in range(0,ROWS):
    for col in range(0, COLS):
        for ch in range(0,CH):
            if (ch == 0):   
                imgR[row,col,ch] = img[row,col,ch] + 100
                

#Grafico el resultado
plt.imshow(imgR,vmin=0, vmax=255)
plt.show                