class Color:
    def __init__(self,color):
        self.color = color
    
    @property
    def recuperar_color(self):
        return self.color

    @recuperar_color.setter
    def modificar_color(self,colorR):
        self._color = colorR