#Etapa 2: Algoritmo para extraer parámetros del video original
import cv2 # OpenCV para computer vision
import numpy as np # Para cálculo de matrices
import matplotlib.pyplot as plt #Para graficar
import os #Habilita el manejo de directorios
import skvideo.io


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

Stack=np.zeros((Frames_number,Fl,Cl,Ch))#Variable para guardar frames del video 
Video.release()

# Etapa 3: Guardando el video
Ruta = r'/home/felipeqg/Documents/Vision-Artificial/assets/videos/rhinos_1.avi'#Ubicación de la imagen desde el google drive
Video = cv2.VideoCapture(Ruta)
i=0
while(Video.isOpened()):
  ret, frame = Video.read () ## ret devuelve un valor booleano
  if ret == True:
    #Aquí agregue el procesamiento de los frames del video
    Stack[i]=frame.astype(np.uint8)
    i=i+1
  else:
    break

skvideo.io.vwrite("/home/felipeqg/Documents/Vision-Artificial/talleres/entregable_2/videosGuardados/Salida.avi", Stack)#Ruta y nombre para guardar
Video.release()
