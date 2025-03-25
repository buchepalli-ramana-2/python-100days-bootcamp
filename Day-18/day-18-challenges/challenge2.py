#Drawing dashed lines
#https://docs.python.org/3/library/turtle.html#turtle.pendown
import turtle as t

tim = t.Turtle()
tim.shape("turtle")
tim.color("red")

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


scr = t.Screen()
scr.exitonclick()