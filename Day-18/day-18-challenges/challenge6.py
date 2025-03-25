# Import the turtle library for 
# drawing the required curve
import turtle as tt
import random

# Set the background color as black,
# pensize as 2 and speed of drawing 

tt.pensize(2)
tt.speed(10)
screen = tt.Screen()
screen.colormode(255)
tt.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_colour = (int(r),int(g),int(b))
    return random_colour


def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tt.color(random_color())
        tt.circle(100)
        tt.setheading(tt.heading() + size_of_gap)

draw_spirograph(5)


'''
#Second method
for i in range(36):
    tt.color(random_color())
    tt.circle(100)
    tt.left(10)

'''

screen.exitonclick()