'''
Based on a user's order, work out their final bill. 
Use the input() function ro get a user's preferences and then add up the total
for their order and tell them houwm much they have to pay.

Here are rates:

Small pizza(S): $15
Medium Pizza(M): $20
Large pizza(L): $25
Add pepperoni for small pizza (Y or N): +$2
Add pepperoni for medium of large pizza (Y or N): $3
Add pepperoni for medium of large pizza (Y or N): $3
Add extra cheese for any size pizza(Y or N): +$1

Example Interaction:

Welcome to python Pizza Deliveries:
What size pizza do you want? S,M or L: L
Do you want peperoni on your pizza? Y or N: Y
Do you want extra cheese? Y or N: N
Your final bill is: $

'''

print("Welcome to python pizza Deliveries.!!!!")
size = input("What size pizza fo you want? S, M or L: ")

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Selected size is not exist")

pepperoni = input("Do you want pepeeroni on your pizza? Y or N: ")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill +=3

cheese = input("DO you want extra cheese? Y or N: ")

if cheese == "Y":
    bill += 1
    
print(f"Your final bill is: ${bill}")