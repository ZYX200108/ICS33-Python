# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions 


from blackhole import Black_Hole
from prey import Prey
import model


class Pulsator(Black_Hole):
    counterConstant = 30
    def __init__(self,x,y):
        Black_Hole.__init__(self,x,y)
        self.radius = 10
        self.pulsatorCounter = 0
        self.removedSet = set()
    
    def update(self):
        self.pulsatorCounter += 1
        object = model.find(lambda x: isinstance(x,Prey))
        if self.radius == 0:
            model.remove(self)
        else:
            if self.pulsatorCounter < Pulsator.counterConstant:
                for x in object:
                    if self.contains(x.get_location()):
                        self.pulsatorCounter = 0
                        self.removedSet.add(x)
                        self.radius += 1
                        self.change_dimension(1,1)
                        model.remove(x)
            else:
                self.change_dimension(-1,-1)
                self.radius -= 1
                self.pulsatorCounter = 0
        # print(self._width,self._height)
        
    def contains(self,xy):
        return self.distance(xy) < self.radius
        
    
    def display(self,canvas):
       canvas.create_oval(self._x-self.radius      , self._y-self.radius,
                                self._x+self.radius, self._y+self.radius,
                                fill="#000000")
