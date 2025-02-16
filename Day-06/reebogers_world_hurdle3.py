    
#The functions move() and turn_left().
#The conditions front_is_clear() or wall_in_front(), at_goal(), and their negation.
#How to use a while loop and an if statement.

# Below code will work only in Reeborg's world website only

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
  
while not at_goal():
    if wall_in_front():
        jump()
    elif front_is_clear():
        move()
    elif at_goal():
        break


