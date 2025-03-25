# Draw different shapes and  each shape with different colors

import turtle as t
import random
colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]
directions = [0,90,180,270]

tim = t.Turtle()
tim.shape("turtle")
tim.pensize(10)
tim.speed(10)

for i in range(200):
    tim.setheading(random.choice(directions))
    tim.color(random.choice(colors))
    tim.forward(30)

screen = t.Screen()
screen.exitonclick()