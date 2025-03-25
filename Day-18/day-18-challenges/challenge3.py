# Draw different shapes and  each shape with different colors
import turtle as t
import random
colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]

tim = t.Turtle()
tim.shape("turtle")


angles = [90,72,60,45,36,30]

# for i in angles:
#     tim.color(colors[angles.index(i)])
#     for _ in range(int(360/i)):
#         tim.forward(100)
#         tim.right(i)

def shapes(num_shapes_n):
    angle = 360 / num_shapes_n
    for i in range(num_shapes_n):
        tim.forward(100)
        tim.right(angle)

for num_shapes in range(3,11):
    tim.color(random.choice(colors))
    shapes(num_shapes)

# screen = t.Screen()
# screen.exitonclick()