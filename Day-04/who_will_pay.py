'''
suppose group of friends went to restaunrant and they want to select one frind to pay the bill.
how you can solve the problem with python

'''
import random 
friends = ["Alice","Bob","Charlie","David","Emanuel"]

# 1st option, to get random item from list
print(random.choice(friends))

#2nd option, to get random item from list
random_number = random.randint(0,len(friends)-1)

print(friends[random_number])

