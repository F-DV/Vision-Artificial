import numpy as np
import cv2
import matplotlib.pyplot as plt

#Leer el path de la imagen con opencv
img_raw = cv2.imread('/home/felipeqg/Documents/Vision-Artificial/assets/mandrill_colour.png')
    
#Cambiar la imagen a matriz con numpy
type(img_raw)
np.ndarray

#Redimensionar la imagen
img_raw.shape
(1300,1950,3)

#Guardar imagen en el directorio de trabajo
#cv2.imwrite('final-image.png',img_raw)

#Cambiar de BGR de openCv a RGB de matplotlib
img = cv2.cvtColor(img_raw, cv2.COLOR_BGR2RGB)

#Dibujar la imagen con matplotlib
plt.imshow(img_raw)

#print('Break point')