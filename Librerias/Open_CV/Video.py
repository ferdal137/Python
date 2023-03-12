import cv2

captura = cv2.VideoCapture(0) #("videoSalida.avi") para visualizar, en lugar de (0)
#salida = cv2.videoWriter("videoSalida.avi", cv2.VideoWriter_fourcc(*"XVID"),20.0,(640,480))

while(captura.isOpen):
    ret,imagen = captura.read()
    if ret==True:
        cv2.inShow("video",imagen)
        #salida.write(imagen)
        if cv2.waitKey(1) & 0xFF == ord ("s"): #Aumentar el número (1) para ver más largo el video 
            break
    
    #else:break (ver video)

captura.release()
#salida.release() 
cv2.destroyAllWindows