
def greet():
    print("First line")
    print("Second line")
    print("Third line")

greet()

def greet(name):
    print(f"Hello {name}")
    print(f"How are you {name}")
    print(f"Isn't weather pleasent {name}")
    
greet("Pessi")
greet(input("Enter name of person that you want to wish: "))


# Parameters and arguments. 
# In the below name,location are parameters and what ever the values pass to the fucntion while calling are arguments

# positional arguments: we will pass the values in the same order as we given function definiton.
def greet(name,location):
    print(f"Hello {name}")
    print(f"How is your {location} location")
print("----------------------------------------")
print("When we are using positional arguments")
print("----------------------------------------")
greet("Ramana","Hyderabad") 
# output looks like when we pass the same order
# Hello Ramana
# How is your Hyderabad location
greet("Ongole","Ramana")
#output looks like below when we miss the order of arguments
#Hello Ongole
#How is your Ramana location

#keyword arguments: no matter of the order or position of the arguments
print("\n")
print("----------------------------------------")
print("When we are using keyword arguments")
print("----------------------------------------")
greet(name="Ramana",location="Hyderabad")
greet(location="Ongole",name="Ramana")
