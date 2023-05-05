#Cargando librerías
import cv2 # OpenCV para computer vision
import numpy as np # Para cálculo de matrices
import matplotlib.pyplot as plt #Para graficar
import os #Habilita el manejo de directorios

#Leyendo imagen de entrada
Ruta = r'/home/felipeqg/Documents/Vision-Artificial/assets/images/fichas.png' #Ubicación de la imagen desde el google drive
Imagen = cv2.imread(Ruta)#Lee
Imagen=Imagen[:,:,[2,1,0]]#Organiza

# Mostramos imagen Original
print('Mostrando imagen de entrada')
plt.imshow(Imagen.astype('uint8'),vmin=0, vmax=255) #Muestra
plt.show()
print('')

#Mostrando cada canal de color y transformanndo a grises
Rojo=Imagen[:,:,0]
print('Canal rojo')
plt.imshow(Rojo.astype('uint8'),vmin=0, vmax=255,cmap='gray')
plt.show()
print('')

Verde=Imagen[:,:,1]
print('Canal verde')
plt.imshow(Verde.astype('uint8'),vmin=0, vmax=255,cmap='gray')
plt.show()
print('')

Azul=Imagen[:,:,2]
print('Canal azul')
plt.imshow(Azul.astype('uint8'),vmin=0, vmax=255,cmap='gray')
plt.show()
print('')

Gris=cv2.cvtColor(Imagen, cv2.COLOR_BGR2GRAY)
print('Grises')
plt.imshow(Gris.astype('uint8'),vmin=0, vmax=255,cmap='gray')
plt.show()
print('')

#Identificamos fichas de color naranja
[Fl, Cl, Ch]=Imagen.shape
Bin_Naranja = np.zeros((Fl,Cl,Ch))
Bin_Naranja = Rojo > 195

print('Region Naranja')
plt.imshow(Bin_Naranja.astype('uint8'),vmin=0, vmax=1,cmap='gray')
plt.show()
print('')

#Multiplicamos el valor unico escogido para cada canal y mostramos
Resultado_Naranja = np.zeros((Fl,Cl,Ch))
Resultado_Naranja[:,:,0]=Imagen[:,:,0]*Bin_Naranja
Resultado_Naranja[:,:,1]=Imagen[:,:,1]*Bin_Naranja
Resultado_Naranja[:,:,2]=Imagen[:,:,2]*Bin_Naranja

print('Fichas Naranja')
plt.imshow(Resultado_Naranja.astype('uint8'),vmin=0, vmax=255)
plt.show()
print('')

# Mejoramos no dando un valor unico si no condicionando los valores
# Segun el canal
[Fl, Cl, Ch]=Imagen.shape
Resultado_Naranja = np.zeros((Fl,Cl,Ch))
Bin_Naranja = np.zeros((Fl,Cl,Ch))
Bin_Naranja = (Rojo > 190)*(Verde < 100)*(Azul < 100)
print('Region Naranja')
plt.imshow(Bin_Naranja.astype('uint8'),vmin=0, vmax=1,cmap='gray')
plt.show()
print('')

Resultado_Naranja[:,:,0]=Imagen[:,:,0]*Bin_Naranja
Resultado_Naranja[:,:,1]=Imagen[:,:,1]*Bin_Naranja
Resultado_Naranja[:,:,2]=Imagen[:,:,2]*Bin_Naranja
print('Fichas Naranja')
plt.imshow(Resultado_Naranja.astype('uint8'),vmin=0, vmax=255)
plt.show()
print('')

# Ahora buscamos las fucsias

[Fl, Cl, Ch]=Imagen.shape
Resultado_Fucsia = np.zeros((Fl,Cl,Ch))
Bin_Fucsia = np.zeros((Fl,Cl,Ch))
Bin_Fucsia = (Rojo > 140)*(Rojo < 170)*(Verde < 80)*(Verde > 40)*(Azul > 90)*(Azul < 135)
print('Region Fucsia')
plt.imshow(Bin_Fucsia.astype('uint8'),vmin=0, vmax=1,cmap='gray')
plt.show()
print('')

Resultado_Fucsia[:,:,0]=Imagen[:,:,0]*Bin_Fucsia
Resultado_Fucsia[:,:,1]=Imagen[:,:,1]*Bin_Fucsia
Resultado_Fucsia[:,:,2]=Imagen[:,:,2]*Bin_Fucsia
print('Fichas Fucsia')
plt.imshow(Resultado_Fucsia.astype('uint8'),vmin=0, vmax=255)
plt.show()
print('')

