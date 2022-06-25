"""
    The special class allows users to put down balls that changes colors constantly.
    After the button is clicked, user can put down balls that changes colors on
    on the place where the mouse is being clicked.
"""
from ball import Ball

class Special(Ball):
    def __init__(self,x,y):
        self.color = 'black'
        Ball.__init__(self, x, y)
        self.colorList = ["#0000FF", "#F0F8FF", "#E3CF57", "#8A2BE2", "#7FFF00", "#FFF8DC", "#FF1493", "#FF6A6A","#7CFC00"]
        self.colorIndex = 0
        
    def update(self):
        self.move()
        try:
            self.color = self.colorList[self.colorIndex]
            self.colorIndex += 1
        except IndexError:
            self.colorIndex = 0
    
    def display(self,canvas):
       canvas.create_oval(self._x-self.radius      , self._y-self.radius,
                                self._x+self.radius, self._y+self.radius,
                                fill=self.color)