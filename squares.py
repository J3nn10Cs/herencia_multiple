from geometricfigures import GeometricFigures
from colors import Color

class Squares(GeometricFigures,Color):
  def __init__(self, side, color):
    GeometricFigures.__init__(self,side,side)
    Color.__init__(self,color)
  
  def calculate_area(self):
    return self.height * self.width

  def __str__(self):
    return f'''
      El area es : {self.calculate_area()}
      El color del cuadrado es : {self.namecolor}
      Los lados del cuadrado son : {self.height} -- {self.width}
    '''

if __name__ == '__main__':
  square1 = Squares(3,'Azul')
  print(square1)