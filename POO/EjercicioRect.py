#Rectangulo
"""
class rectangulo:
    def __init__(self,base,altura):
        self.altura = altura
        self.base = base

    def area(self):
        area = self.altura * self.base
        print(f"El área del rectángulo es: {area}")

base = int(input("Ingrese la base: "))
altura = int(input("Ingrese la altura: "))

rec = rectangulo(base,altura)
rec.area()"""

#Cubo

class cubo:

    def __init__(self,ancho,alto,deep):
        self.alto = alto
        self.ancho = ancho
        self.deep = deep

    def volumen(self):
        v = self.alto * self.ancho * self.deep
        print(f"El volumen del cubo es: {v}")

ancho = int(input("Ingrese el ancho: "))
alto = int(input("Ingrese el alto: "))
deep = int(input("Ingrese la profundidad: "))

c = cubo(ancho, alto, deep)
c.volumen()