# The robot has to reach the destination by crossing all hurdles.
# This code will work only reeborg's world website 
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

def jump():
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()

def move_fwd():
    move()
    turn_left()
    
for t in range(6):
        move_fwd()
        jump()