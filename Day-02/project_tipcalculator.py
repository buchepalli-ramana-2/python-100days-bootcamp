'''
Title: Tip Calculator
Description: A group of friends went to restaunrent. 
Bill has to split among them which include tip of some % on total bill.

python program should be able to:
Ask user to enter the bill amount,give options % of tip want to give and how many people has to share the bill.

program has to give amount of each person should pay.

'''
print("Welcome to the Tip Calculator!!")
bill_amount = int(input("What was total bill amount? $ "))
tip = int(input(f"How much tip would you like give? 10 12 or 15? "))
people= int(input(f"How many people split the bill? "))
each_pay = (bill_amount + (bill_amount * (tip/100)))/people
each_pay = round(each_pay,2)
print(f"Each person should pay: ${each_pay}")
