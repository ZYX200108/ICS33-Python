# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 


#from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random, uniform
import math


class Floater(Prey):
    radius = 5
    def __init__(self, x, y):
        # dimension = self.get_dimension()
        angle = 2*math.pi*random()
        Prey.__init__(self, x, y, 10, 10, angle, speed=5)
        
    def update(self):
        self.move()
        randomNum = random()
        angle = self.get_angle()
        speed = self.get_speed()
        if randomNum < 0.3:
            randomNum2 = uniform(-0.5, 0.5)
            if 3 <= speed + randomNum2 <= 7:
                self.set_angle(angle + uniform(-0.5, 0.5))
                self.set_speed(speed + randomNum2)
            
    def display(self,canvas):
       canvas.create_oval(self._x-Floater.radius      , self._y-Floater.radius,
                                self._x+Floater.radius, self._y+Floater.radius,
                                fill="#FF0000")
