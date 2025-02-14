# What is Module? -  A module is a file containing Python definitions and statements. 
# The file name is the module name with the suffix .py appended. Refer https://docs.python.org/3/tutorial/modules.html

# Import random module. 
import random

# Print random integer between 1 and 10.
random_integer = random.randint(1,10)
print(random_integer)

# Print random float number between 0 to 1
random_float_0_1 = random.random()
print(random_float_0_1)

# Print random number between given range
random_float = random.uniform(1, 10)
print(random_float)

# I want to Toss then get the random Heads or Tails
random_heads_or_tails = random.randint(0,1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")

