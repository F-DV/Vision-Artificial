import cv2 # OpenCV para computer vision
import numpy as np # Para cálculo de matrices
import matplotlib.pyplot as plt #Para graficar
import skvideo.io


#Ejemplo con la imagen de lena para unir 3 frames
"""
Ruta1 = r'/home/felipeqg/Documents/Vision-Artificial/assets/images/Lena.png' # Path de imagen 
Ruta2 = r'/home/felipeqg/Documents/Vision-Artificial/assets/images/Lena.png'
Ruta3 = r'/home/felipeqg/Documents/Vision-Artificial/assets/images/Lena.png'

Imagen1 = cv2.imread(Ruta1)
Imagen2 = cv2.imread(Ruta2)
Imagen3 = cv2.imread(Ruta3)

Imagen2=Imagen2[:,:,[2,1,0]]#Organiza imagen
Imagen3=Imagen3[:,:,[2,1,0]]#Organiza imagen

Imagen2 = cv2.cvtColor(Imagen2,cv2.COLOR_BGR2GRAY)# Imagen a grises

#Nuevo frame para las tres imagenes
[Fl, Cl, Ch]=Imagen1.shape #Leo el tamaño de 1 de las imagenes
newFrame =np.zeros((Fl,Cl*3,Ch))# creo una matriz con el triple de tamaño en filas y columnas para el nuevo frame
ROWS = Fl
COLS = Cl*3

print('Tamaño Imagen original: ', Fl,Cl)
print('Tamaño Imagen newFrame: ', ROWS,COLS)

#for para aderir la imagen 1 al new frame
for col in range(0,COLS):
    for row in range(0,ROWS):
            for ch in range(0,Ch):
                if col < Cl:             
                    newFrame[row,col,ch] = Imagen1[row,col,ch]

#for para aderir la imagen 2 al new frame
for col in range(440,880):
    for row in range(0,ROWS):
            for ch in range(0,Ch):                   
                newFrame[row,col,ch] = Imagen3[row,col-440,ch]

#for para aderir la imagen 3 al new frame
for col in range(880,1320):
    for row in range(0,ROWS):
            for ch in range(0,Ch):                   
                newFrame[row,col,ch] = Imagen2[row,col-880]


print('New Frame')
plt.imshow(newFrame.astype('uint8'),vmin=0, vmax=255,cmap='gray') #Grafica la imagen
plt.figure(figsize=(20,20))
plt.show()
print('')
"""

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

print('Tamaño Imagen original: ', Fl,Cl)
print('Tamaño Imagen newFrame: ', ROWS,COLS)

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

skvideo.io.vwrite("/home/felipeqg/Documents/Vision-Artificial/talleres/entregable_2/videosGuardados/Salida3.avi", Stack)#Ruta y nombre para guardar
Video.release()
