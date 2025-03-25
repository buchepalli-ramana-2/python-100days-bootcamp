# Create circle with turtle
from turtle import Turtle, Screen

tummy_the_turtle = Turtle()
tummy_the_turtle.shape("turtle")
tummy_the_turtle.color("Green")

for i in range(4):
    tummy_the_turtle.forward(200)
    tummy_the_turtle.right(90)


# Exit the screen on click
screen = Screen()
screen.exitonclick()