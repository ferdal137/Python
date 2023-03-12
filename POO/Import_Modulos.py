from Encapsulamiento import Persona

print("Creación de objetos".center(50,"-"))
persona1 = Persona("Karla","Gómez", 34)
persona1.mostrar_detalle()

print("Eliminación de objetos".center(50,"-"))
del persona1 #Eliminar objeto