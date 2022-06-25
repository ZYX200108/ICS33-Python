# This Black_Hole class is derived from Simulton; for updating it finds+removes
#   objects (of any class Prey derived class) whose center is contained inside
#   its radius (returning a set of all eaten simultons), and it displays as a
#   black circle with a radius of 10 (width/height 20).
# Calling get_dimension for the width/height (for containment and displaying)'
#   will facilitate inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
import model


class Black_Hole(Simulton):  
    radius = 10
    
    def __init__(self,x,y):
        Simulton.__init__(self,x,y,20,20)
        self.removedSet = set()
        
    def contains(self,xy):
        return self.distance(xy) < Black_Hole.radius
        
    def update(self):
        object = model.find(lambda x: isinstance(x,Prey))
        for x in object:
            if self.contains(x.get_location()):
                self.removedSet.add(x)
                model.remove(x)
        return self.removedSet
    
    def display(self,canvas):
       canvas.create_oval(self._x-Black_Hole.radius      , self._y-Black_Hole.radius,
                                self._x+Black_Hole.radius, self._y+Black_Hole.radius,
                                fill="#000000")