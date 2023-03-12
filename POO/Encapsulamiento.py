# Encapsulamiento
# Nota : Las variables de solo lectura no tienen el método set

class Persona:
    def __init__(self,nombre,apellido,edad): #Método tipo dunder por el doble guión bajo
        self._nombre = nombre 
        """No se deberia acceder (imprimir) a este atributo mediante el objeto ni modificar
        sus valores pero es psoible (A esto se le conoce como atributo encapsulado).
        Si ponemos doble guión bajo (__nombre) es imposible acceder desde el objeto"""
        self._apellido = apellido
        self._edad = edad
        
    
    #GET (Recuperar elemento)
    @property #Decorador
    def recuperar_nombre(self):
        #print("Llamando método get recuperar_nombre(")
        return self._nombre
    
    #Set (Modificar valor)
    @recuperar_nombre.setter
    def modificar_nombre(self,nombreRecibido):
        #print("Llamando método set modificar_nombre")
        self._nombre = nombreRecibido

    @property
    def recuperar_apellido(self):
        return self._apellido
    
    @recuperar_apellido.setter
    def modificar_apellido(self,apellidoRecibido):
        self._apellido = apellidoRecibido

    @property
    def recuperar_edad(self):
        return self._edad

    @recuperar_edad.setter
    def modificar_edad(self,edadRecibida):
        self._edad = edadRecibida



    def mostrar_detalle(self):
        print(f"Persona: {self._nombre} {self._apellido} {self._edad}")

    def __del__(self):
        print(f"Persona: {self._nombre} {self._apellido}")


if __name__ == "__main__" : 

    persona1 = Persona("Juan" ,"Perez",28)
    #print(persona1.recuperar_nombre) #No son necesarios los parentesis por el decorador
    persona1.mostrar_detalle()

    persona1.modificar_nombre = "Juan Carlos"
    persona1.modificar_apellido = "Perez Hernandez"
    persona1.modificar_edad = 30
    persona1.mostrar_detalle()

    print(__name__)