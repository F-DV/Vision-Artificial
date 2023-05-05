
############## IMAGEN DETECCION DE BORDES DE MESSI ###############

""" 
Filtramos la imagen de Messi con el filtro
medianBlur para quitarle el ruido ya que fue el mas efectivo, luego pasamos la imagen
resultande a grises para aplicarvla funcion de opencv Sobel para detectar bordes

"""

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

"""