(Bordes_Am,_) =cv2.findContours(Opened_Amarillas, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
if len(Bordes_Am)==4:
  print('Usted tiene '+ str(len(Bordes_Am))+' fichas de color amarillo, están completas.')
else:
    if len(Bordes_Am)<4:
      print('Usted tiene ' + str(len(Bordes_Am)) + ' fichas de color amarillo, hacen falta ' + str(4-len(Bordes_Am))+' fichas para el paquete.')
    else:
      if len(Bordes_Am)>4:
         print('Usted tiene ' + str(len(Bordes_Am)) + ' fichas de color amarillo, sobran ' + str(len(Bordes_Am)-4)+' fichas.')