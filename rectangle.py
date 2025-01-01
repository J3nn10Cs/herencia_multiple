from geometricfigures import GeometricFigures
from colors import Color

class Rectangle(GeometricFigures,Color):
  def __init__(self, height, width,color):
    GeometricFigures.__init__(self,height,width)
    Color.__init__(self,color)
  
  def calculate_area(self):
    return self.height * self.width

  def name_colors(self):
    return self.name_colors
  
  def __str__(self):
    return f'''
      El area del rectangulo es : {self.calculate_area()}
      El color del rectanguo es : {self.namecolor}
      Los lados del rectangulo es : {self.height} - {self.width}
    '''

if __name__ == '__main__':
  rentamgle1 = Rectangle(4,5,'Morado')
  print(rentamgle1)