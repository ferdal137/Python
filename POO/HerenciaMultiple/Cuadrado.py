from Figura import FiguraGeo
from Color import Color

class Cuadrado(FiguraGeo,Color):
    def __init__(self,base,altura,color):
        #super().__init__(base, altura) #No se usa ya que solo mandaria llamar a la pirmer clase padre (FiguraGeo)
        FiguraGeo.__init__(self,base,altura)
        Color.__init__(self,color)

    def calcularArea(self):
        return self._base * self._altura
