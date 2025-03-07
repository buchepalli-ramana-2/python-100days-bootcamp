# Importing the turtle module
# import prettytable
'''
from turtle import Turtle, Screen
timmy = Turtle()
timmy.shape("turtle")
timmy.color("LightSalmon3")

my_screen = Screen()
# print(my_screen.canvheight)

# turtle moving forward
print(timmy.forward(100))
my_screen.exitonclick()

'''
# Install prettytable package using 'pip install prettytable' command. 
# create a ASCII table for pokeman name and Type of it.

#Importing PrettyTable class from prettytable package
from prettytable import PrettyTable

#assign the prettytable method or attribute to variable name table
table = PrettyTable()

# Adding two columns
table.add_column("Pokeman Name",["Fennekin","Froakie","Talonflame"])
table.add_column("Type",["Fire","water","Flying"])

#aligning the data in table to "l" - left, "r" - "right", "c" - "center".
table.align = "c"
print(table)