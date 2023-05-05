"""
Segmentación y clasificación de imágenes por color

Adjunto encontrará una base de datos con 30 imágenes con diferentes cosas 
(frutas, verduras, entre otras).

Realice una estrategia de segmentación por color que permita clasificar los tipos de objetos en las imágenes.

Realice una estrategia de validación para determinar qué tan eficiente es el método desarrollado, es decir, 
determinar cuántas imágenes clasifica bien. El resultado debe entregarse en porcentaje o así: X/30. 

Use clasificación por color y operaciones morfologicas.

El esquema de segmentación debe ser completamente automático, es decir, leer todas las imágenes y 
decir qué objeto hay en cada imagen.

Adjunte un notebook que realice todo lo solicitado y entrege el resultado de desempeño.

El código se probará con imágenes nuevas del mismo tipo.
"""

#Cargando librerías
import cv2 # OpenCV para computer vision
import numpy as np # Para cálculo de matrices
import matplotlib.pyplot as plt #Para graficar
import os #Habilita el manejo de directorios

#Leyendo imagen de entrada
Ruta = r'/home/felipeqg/Documents/Vision-Artificial/talleres/reto2/dataset/jalapeno_1.jpg' #Ubicación de la imagen 
ImagenO = cv2.imread(Ruta)#Lee

"""
#Leerimagenes de una carpeta
folderPath = '/home/felipeqg/Documents/Vision-Artificial/talleres/reto2/dataset' 
file_names = os.listdir(folderPath)

for file in file_names:
    imagen_path = '/home/felipeqg/Documents/Vision-Artificial/talleres/reto2/dataset/'+ file
    print(imagen_path)
    image = cv2.imread(imagen_path)
    plt.imshow(image.astype('uint8'),vmin=0, vmax=255)
    #cv2.imshow('Image',image)
    #cv2.waitKey(0)
    #print(file)
    
"""

#Extracción de canales en HSV y BGR
Imagen= cv2.cvtColor(ImagenO,cv2.COLOR_BGR2RGB)
Imagen_hsv = cv2.cvtColor(ImagenO,cv2.COLOR_BGR2HSV)

#Tamaño de la imagen
[Fl,Cl,Ch] = Imagen.shape

#Espectro visible en hsv
#Se crean 2 matricez uno para los valores bajos y otro para los altos
#manzanas rojas
rojoBajo = np.array([0,50,50],np.uint8)
rojoAlto = np.array([15,255,255],np.uint8)
mascara1 = cv2.inRange(Imagen_hsv,rojoBajo,rojoAlto)

"""#Manzanas casi naranjas
rojoMaduroBajo = np.array([0,140,140],np.uint8)
rojoMaduroAlto= np.array([30,200,200],np.uint8)
mascara1 = cv2.inRange(Imagen_hsv,rojoMaduroBajo,rojoMaduroAlto)
"""
# Bananas
amarilloBajo = np.array([20,50,50],np.uint8)
amarilloAlto = np.array([32,255,255],np.uint8)
mascara2 = cv2.inRange(Imagen_hsv,amarilloBajo,amarilloAlto)

# Carrots
naranjaBajo = np.array([15,82,82],np.uint8)
naranjaAlto = np.array([35,255,255],np.uint8)
mascara3 = cv2.inRange(Imagen_hsv,naranjaBajo,naranjaAlto)

# garlic
beigeBajo = np.array([10,0,0],np.uint8)
beigeAlto = np.array([24,245,239],np.uint8)
mascara4 = cv2.inRange(Imagen_hsv,beigeBajo,beigeAlto)

# grapes
purpleBajo = np.array([100,50,50],np.uint8)
purpleAlto = np.array([176,255,255],np.uint8)
mascara5 = cv2.inRange(Imagen_hsv,purpleBajo,purpleAlto)

# Jalapeno
greenBajo = np.array([40,50,50],np.uint8)
greenAlto = np.array([75,255,255],np.uint8)
mascara6 = cv2.inRange(Imagen_hsv,greenBajo,greenAlto)

#Operacion Morfologica posibles kenerls a usar
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
kernel1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
kernel2 = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))

result = cv2.morphologyEx(mascara1,cv2.MORPH_CLOSE,kernel)
result2 = cv2.morphologyEx(mascara2,cv2.MORPH_CLOSE,kernel)
result3 = cv2.morphologyEx(mascara3,cv2.MORPH_CLOSE,kernel)
result4 = cv2.morphologyEx(mascara4,cv2.MORPH_CLOSE,kernel)
result5 = cv2.morphologyEx(mascara5,cv2.MORPH_CLOSE,kernel)
result6 = cv2.morphologyEx(mascara6,cv2.MORPH_CLOSE,kernel)

#Contornos
contornoApple,_ = cv2.findContours(result,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
contornoBanana,_ = cv2.findContours(result2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
contornoCarrot,_ = cv2.findContours(result3,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
contornoGarlic,_ = cv2.findContours(result4,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
contornoGrapes,_ = cv2.findContours(result5,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
contornoJalapeno,_ = cv2.findContours(result6,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

#Banderas
manzana = False
banana = False
carrot = False
garlic = False
grapes = False
jalapeno = False

#Region con porcentage mayor a 60% 
areaEnBlancoApple = 0.0
for c in contornoApple:
    area = cv2.contourArea(c)
    areaEnBlancoApple = areaEnBlancoApple + area 
    
    if(((100 * areaEnBlancoApple)/(Fl*Cl)) >= 25): #filtro
        manzana = True
      
#Region con porcentage mayor a 60% 
areaEnBlancoBanana = 0.0
for c in contornoBanana:
    area1 = cv2.contourArea(c)
    areaEnBlancoBanana= areaEnBlancoBanana + area1 
    
    if(((100 * areaEnBlancoBanana)/(Fl*Cl)) > 6): #filtro
        banana = True
        
#Region con porcentage mayor a 60% 
areaEnBlancoCarrot = 0.0
for c in contornoCarrot:
    area2 = cv2.contourArea(c)
    areaEnBlancoCarrot= areaEnBlancoCarrot + area2 
    
    if(((100 * areaEnBlancoCarrot)/(Fl*Cl)) > 6 and (manzana !=True)): #filtro
        carrot = True
       
#Region con porcentage mayor a 60% 
areaEnBlancoGarlic = 0.0
for c in contornoGarlic:
    area3 = cv2.contourArea(c)
    areaEnBlancoGarlic= areaEnBlancoGarlic + area3 
    
    if(((100 * areaEnBlancoGarlic)/(Fl*Cl)) >=23.8): #filtro
        garlic = True
   
#Region con porcentage mayor a 60% 
areaEnBlancoGrapes= 0.0
for c in contornoGrapes:
    area4 = cv2.contourArea(c)
    areaEnBlancoGrapes= areaEnBlancoGrapes + area4 
    
    if(((100 * areaEnBlancoGrapes)/(Fl*Cl)) > 6 ): #filtro
        grapes = True

#Region con porcentage mayor a 60% 
areaEnBlancoJalapeno= 0.0
for c in contornoJalapeno:
    area5 = cv2.contourArea(c)
    areaEnBlancoJalapeno = areaEnBlancoJalapeno + area5 
    
    if(((100 * areaEnBlancoJalapeno)/(Fl*Cl)) > 6 ): #filtro
        jalapeno = True
 
   
#Validando la fruta             
if(manzana):
    print('Es una manzana')
if(banana):
    print('Es una banana')  
if(carrot):
    print('Es Zanahoria')  
if(garlic):
    print('Es Ajo') 
if(grapes):
    print('Son uvas') 
if(jalapeno):
    print('Es Jalapeno') 
     
print('Pixeles en total de la imagen: ',Fl*Cl)
print('pixeles en blanco: ',areaEnBlancoJalapeno)
print('porcentage de total en blanco',((100 * areaEnBlancoJalapeno)/(Fl*Cl)))

print('Imagen HSV')
plt.imshow(Imagen_hsv.astype('uint8'),vmin=0, vmax=255)
plt.show()
plt.imshow(result6.astype('uint8'),vmin=0, vmax=255,cmap='gray')
plt.show()




