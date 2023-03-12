import cv2 

imagen = cv2.imread("logo.png",0) # Transfomar a escala de grises (1 color)

cv2.imshow("Prueba de imagen",imagen)

cv2.imwrite("logoGrises.jpg",imagen)

cv2.waitKey(3000) #Presionar tecla salir

cv2.destroyAllWindows()