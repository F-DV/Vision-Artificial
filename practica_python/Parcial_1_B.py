"""
APlicar contraste
#################### IMAGEN Parcial_1_B.jpg #####################

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

print('Imagen Resultado_2')
plt.imshow(res.astype('uint8'),vmin=0, vmax=255) #Grafica la imagen
plt.show()
print('')

"""