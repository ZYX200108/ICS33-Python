import controller
import model   # Calling update in update_all passes a reference to this model

#Use the reference to this module to pass it to update methods

from ball      import Ball
from blackhole import Black_Hole
from floater   import Floater
from hunter    import Hunter
from pulsator  import Pulsator
from special   import Special


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running     = False
cycle_count = 0
balls       = set()
buttonClicked = ''


#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running,cycle_count,balls
    running     = False
    cycle_count = 0
    balls       = set()


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#step just one update in the simulation
def step ():
    global cycle_count, running
    if running:
        cycle_count += 1
        for b in balls:
            b.update()
        running = False
    else:
        running = True
        cycle_count += 1
        for b in balls:
            b.update()
        running = False


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global buttonClicked
    buttonClicked = kind
    


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    global buttonClicked, balls
    if buttonClicked == 'Remove':
        for i in list(balls):
            if (x - 10 <= i.get_location()[0] <= x + 10) and (y - 10 <= i.get_location()[1] <= y + 10):
                remove(i)
    else:
        add(eval('{}(x,y)'.format(buttonClicked)))



#add simulton s to the simulation
def add(s):
    balls.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    balls.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    set_return = set()
    for i in balls:
        if p(i):
            set_return.add(i)
    return set_return


#For each simulton in model's simulation, call update on it, passing along model
#This function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton's update do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def update_all():
    global cycle_count
    if running:
        cycle_count += 1
        for b in list(balls):
            b.update()

#Animation: (a) delete all simultons on the canvas; (b) call display on all
#  simultons being simulated, adding back each to the canvas, often in a new
#  location; (c) update the label defined in the controller showing progress 
#This function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for b in balls:
        b.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(str(cycle_count)+" cycles/" + str(len(balls))+" simultons"))
