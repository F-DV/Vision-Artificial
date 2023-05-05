#Cargando librerías
import cv2 # OpenCV para computer vision
import numpy as np # Para cálculo de matrices
import matplotlib.pyplot as plt #Para graficar
import skvideo.io

#=====================PUNTO 1 DETECCION DE BORDES ==================
RutaImagenBordes = r'/home/felipeqg/Documents/Vision-Artificial/assets/images/imagen_1.JPG' # Path de imagen 
Imagen_1 = cv2.imread(RutaImagenBordes)#Lee imagen 
Imagen_1=Imagen_1[:,:,[2,1,0]]#Organiza imagen

print('Imagen_1 Original')
plt.imshow(Imagen_1.astype('uint8'),vmin=0, vmax=255,cmap='gray') #Grafica la imagen
plt.figure(figsize=(20,20))
plt.show()
print('')
  
imagenFiltrada = cv2.medianBlur(Imagen_1,9) #Filtro 
imagenFiltrada2 = cv2.medianBlur(imagenFiltrada,9) #Filtro 
imagenFiltrada3 = cv2.medianBlur(imagenFiltrada2,9) #Filtro 
imagenFiltrada4 = cv2.medianBlur(imagenFiltrada3,9) #Filtro 

imagenGris = cv2.cvtColor(imagenFiltrada4,cv2.COLOR_BGR2GRAY)# Imagen a grises

sobelX = cv2.Sobel(imagenGris, cv2.CV_64F,1,0)
sobelY = cv2.Sobel(imagenGris, cv2.CV_64F,0,1)
sobelx = np.uint8(np.absolute(sobelX))
sobely = np.uint8(np.absolute(sobelY))

sobelTotal = cv2.bitwise_or(sobelx,sobely)

print('Bordes de Imagen_1')
plt.imshow(sobelTotal.astype('uint8'),vmin=0, vmax=255,cmap='gray') #Grafica la imagen
plt.figure(figsize=(20,20))
plt.show()
print('')

#===================== PUNTO 2 UNIR 3 VIDEOS EN 1  ================
#Leyendo video de referencia
Ruta = r'/home/felipeqg/Documents/Vision-Artificial/assets/videos/rhinos_1.avi'#Ubicación de la imagen desde el google drive
Video = cv2.VideoCapture(Ruta)

#Testeando tamaño de video original
Frames_number=0

while(Video.isOpened()):
  ret, frame = Video.read () ## ret devuelve un valor booleano
  if ret == True:
    Frames_number=Frames_number+1
    
    Color=frame[:,:,[2,1,0]]#Organiza
    
    cv2.imwrite('/home/felipeqg/Documents/Vision-Artificial/talleres/entregable_2/guardarFrames/rhinos_'+str(Frames_number)+'.jpg',Color)
    
    [Fl,Cl,Ch]=Color.shape
    
  else:
      break

Stack=np.zeros((Frames_number,Fl,Cl*3,Ch))#Variable para guardar frames del video 
Video.release()

# Etapa 3: Guardando el video
Ruta1 = r'/home/felipeqg/Documents/Vision-Artificial/assets/videos/rhinos_1.avi'#Ubicación del video 1
Ruta2 = r'/home/felipeqg/Documents/Vision-Artificial/assets/videos/rhinos_2.avi'#Ubicación del video 2
Ruta3 = r'/home/felipeqg/Documents/Vision-Artificial/assets/videos/rhinos_3.avi'#Ubicación del video 3

Video1 = cv2.VideoCapture(Ruta1)#Leer video 1
Video2 = cv2.VideoCapture(Ruta2)#Leer video 2
Video3 = cv2.VideoCapture(Ruta3)#Leer video 3

ret1, frameV1 = Video1.read () # Lee frames del video1

#Nuevo frame para las tres imagenes
[Fl, Cl, Ch] = frameV1.shape # Leo el tamaño y canales de los frames
  
newFrame =np.zeros((Fl,Cl*3,Ch))# creo una matriz con el triple de tamaño en columnas para el nuevo frame
ROWS = Fl
COLS = Cl*3

print('Tamaño Frame original: ', Fl,Cl)
print('Tamaño newFrame: ', ROWS,COLS)

i=0
while(Video1.isOpened()):
  ret1, frameV1 = Video1.read () # Lee frames del video1
  ret2, frameV2 = Video2.read() # Lee frames del video2
  ret3, frameV3 = Video3.read() # Lee frames del video3
  
  if ret1 == True and ret2 == True and ret3 == True:
    #Aquí agregue el procesamiento de los frames del video

    #for para aderir la frame 1 al new frame
    for col in range(0,COLS):
        for row in range(0,ROWS):
                for ch in range(0,Ch):
                    if col < Cl:             
                        newFrame[row,col,ch] = frameV1[row,col,ch]

    #for para aderir el frame 2 al new frame
    for col in range(320,640):
        for row in range(0,ROWS):
                for ch in range(0,Ch):                   
                    newFrame[row,col,ch] = frameV2[row,col-320,ch]

    #for para aderir el frame 3 al new frame
    for col in range(640,960):
        for row in range(0,ROWS):
                for ch in range(0,Ch):                   
                    newFrame[row,col,ch] = frameV3[row,col-640,ch]
    
    Stack[i]=newFrame.astype(np.uint8)
    i=i+1
  else:
    break

#Ruta para guardar el video modificado
skvideo.io.vwrite("/home/felipeqg/Documents/Vision-Artificial/talleres/entregable_2/videosGuardados/Salida.avi", Stack)#Ruta y nombre para guardar
Video.release()

#===================== PUNTO 3 SEGMENTACION RUBIK ================

#Leyendo imagen de cubo rubik de entrada
Ruta = r'/home/felipeqg/Documents/Vision-Artificial/assets/images/rubik.png' #Ubicación de la imagen desde el google drive
Imagen = cv2.imread(Ruta)#Lee
Imagen=Imagen[:,:,[2,1,0]]#Organiza

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
