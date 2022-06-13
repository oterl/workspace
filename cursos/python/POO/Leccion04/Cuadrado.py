# HERENCIA MULTIPLE
#
from FiguraGeometrica import FiguraGeometrica
from Color import Color #si queremos renombrar alguna clase, al final de la sentencia se coloca "as OtroNombre"

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        return self._ancho * self._alto

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'


#
