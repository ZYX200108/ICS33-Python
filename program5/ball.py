# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10). 


from prey import Prey
import math, random


class Ball(Prey): 
    radius = 5
    
    def __init__(self,x, y):
        angle = 2*math.pi*random.random()
        Prey.__init__(self,x, y, 10, 10, angle, 5)
        #self.radius = 5
        #self.colorList = ["#0000FF", "#F0F8FF", "#E3CF57", "#8A2BE2", "#7FFF00", "#FFF8DC"]
        #self.colorIndex = 0
        
    def update(self):
        self.move()

    
    def display(self,canvas):
        # try:
       canvas.create_oval(self._x-self.radius      , self._y-self.radius,
                                self._x+self.radius, self._y+self.radius,
                                fill="#0000FF")
        # except IndexError:
        #     self.colorIndex = 0
    
    # def colorChange(self):
    #     self.colorIndex += 1
