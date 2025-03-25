# Named colours rgb
import turtle as t
import random

colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]

tim = t.Turtle()
tim.shape("turtle")
tim.pensize(10)

screen = t.Screen()
screen.colormode(255)


directions = [0,90,180,270]

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_colour = (int(r),int(g),int(b))
    return random_colour

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))



screen.exitonclick()