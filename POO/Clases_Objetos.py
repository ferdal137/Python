# Clases y objetos

class Persona: #Las clases inician en mayuscula
    def __init__(self,nombre,apellido,edad,*args,**kwargs): #Método tipo dunder por el doble guión bajo
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.args = args
        self.kwargs = kwargs
    
    def mostrar_detalle(self):
        print(f"Persona: {self.nombre} {self.apellido} {self.edad} {self.args} {self.kwargs}")


persona1 = Persona("Juan" ,"Perez",28,2,3,4,m = "manzana",p = "pera")
persona1.telefono = "771123456" #Pero solo persona1 tiene telefono (No recomendable)
persona1.mostrar_detalle() #Llamar al método desde el objeto
#Persona.mostrar_detalle(persona1) #Llamar al método desde la clase

persona2 = Persona("Maria","Hernández",34)
persona2.mostrar_detalle()

