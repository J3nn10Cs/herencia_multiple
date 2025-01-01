class GeometricFigures:
  def __init__(self,width, height):
    self._width = width
    self._height = height
  
  #get
  @property
  def width(self):
    return self._width

  @property
  def height(self):
    return self._height
  
  @width.setter
  def width(self,width):
    self._width = width
  
  @height.setter
  def height(self,height):
    self._height = height
  
  def __str__(self):
    return f'''
      Ancho : {self.width}
      Alto : {self.height}
    '''
