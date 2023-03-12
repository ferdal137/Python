from Figura import FiguraGeo
from Color import Color 

class Rectangulo(FiguraGeo,Color):
    def __init__(self,base,altura,color):
        FiguraGeo.__init__(self,base,altura)
        Color.__init__(self,color)

    def calcularArea(self):
        return self._base * self._altura