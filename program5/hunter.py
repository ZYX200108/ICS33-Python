# The Hunter class is derived from Pulsator first and then Mobile_Simulton.
#   It inherits updating/displaying from Pusator and Mobile_Simulton: it pursues
#   close prey, or moves in a straight line, like its Mobile_Simultion base.


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2,pi
import random
import model


class Hunter(Pulsator, Mobile_Simulton):  
    def __init__(self,x,y):
        angle = 2*pi*random.random()
        Pulsator.__init__(self,x,y)
        Mobile_Simulton.__init__(self,x,y,20,20,angle,5)
    
    def update(self):
        self.move()
        Pulsator.update(self)
        object = model.find(lambda x: isinstance(x,Prey))
        tempDict = {}
        for x in object:
            if self.distance(x.get_location()) < 200:
                tempDict[x] = (self.distance(x.get_location()))
        try:
            purpose = sorted(tempDict.items(), key=lambda x:(x[1]))[0][0]
            newAngle = atan2(purpose.get_location()[1] - self.get_location()[1], purpose.get_location()[0] - self.get_location()[0])
            self.set_angle(newAngle)
            # if Pulsator.contains(self, purpose.get_location()):
            #     model.remove(purpose)
        except IndexError:
            pass
       
        