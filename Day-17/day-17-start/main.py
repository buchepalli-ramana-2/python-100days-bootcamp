# creating empty class
'''
class User:
    pass

# Creating object with Class
user1 = User()

# adding attributes(is an variable that is associated with object) to the class object

user1.name = "Ramana"
user1.id = "345906"
user1.address = "hyderabad"

user2.name = "Prasanna"
user2.id = "861628"
user2.address = "Bangalore"


print(user1.name)
print(user1.id)
print(user1.address)

print(user2.name)
print(user2.id)
print(user2.address)

'''

# What ever the statements inside __init__ function will execute at the time calling class. 
# Here we are creating attributes or variable within class constructor. 
# __init__ function will reduce lines of code to assign values or creating objects using class.


class User:
    def __init__(self, name, id, address):
        self.name = name
        self.id = id
        self.address = address
        self.followers = 0
        self.following = 0
    
    # adding methods to the class
    def follow(self, user):
        user.followers += 1
        self.following += 1

user1 = User("name",345906,"address")
user2 = User("Raj",345907,"secunderbad")

user1.follow(user2)

print(user1.name)
print(user1.id)
print(user1.address)

print(user2.name)
print(user2.id)
print(user2.address)

print(user1.following)
print(user1.followers)

print(user2.following)
print(user2.followers)