from Figura import FiguraGeo
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

# No se puede instanciar una clase abstracta
# figura1 = FiguraGeo()

cuadrado1 = Cuadrado(base = 5,altura = 5,color = "rojo")
print(f"El color del rectángulo es: {cuadrado1.recuperar_color}")
cuadrado1.modificar_base = 8
cuadrado1.modificar_altura = 8
print(f'El área es: {cuadrado1.calcularArea()}')

rectangulo1 = Rectangulo(base = 3,altura = 4,color = "Verde")
rectangulo1.modificar_base = 8
print(f"El color del rectángulo es: {rectangulo1.recuperar_color}")
print(f'El área es: {rectangulo1.calcularArea()}')

#MRO - Metod Resolution Order
#print(Cuadrado.mro()) # Ver en que orden se ejecutan las clasese