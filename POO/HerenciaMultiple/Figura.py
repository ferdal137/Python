from abc import ABC, abstractmethod

class FiguraGeo(ABC):
    def __init__(self,base,altura):
        if self._validar_valor(base):
            self._base = base
        else:
            self._base = 0
            print("Valor erroneo",base)

        if self._validar_valor(altura):
            self._altura = altura
        else:
            self._altura = 0
            print("Valor erroneo",altura)

    
    @property
    def recuperar_base(self):
        return self._base
    
    @recuperar_base.setter
    def modificar_base(self,baseR):
        if self._validar_valor(baseR):
            self._base = baseR 
        else:
            print("Valor erroneo",baseR)

    @property
    def recuperar_altura(self):
        return self._altura
    
    @recuperar_altura.setter
    def modificar_altura(self,alturaR):
        if self._validar_valor(alturaR):
            self._altura = alturaR
        else:
            print("Valor erroneo",alturaR)

    @abstractmethod
    def calcular_area(self):
        pass

    #def __str__(self):
        #return {super().__str__()}

    def _validar_valor(self,valor):
        return True if 0 < valor < 10 else False