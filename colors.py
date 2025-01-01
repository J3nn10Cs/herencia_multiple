class Color:
  def __init__(self,namecolor):
    self._namecolor = namecolor
  
  @property
  def namecolor(self):
    return self._namecolor
  
  @namecolor.setter
  def namecolor(self,namecolor):
    self._namecolor = namecolor
  