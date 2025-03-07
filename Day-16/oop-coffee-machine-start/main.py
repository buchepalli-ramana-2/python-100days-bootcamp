from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

'''
program Requirement:

1. print Report
2. Check Resources sufficient
3. process coins
4. Check transaction successful
5. Make coffee

Go through CoffeeMchineClassessDocumentation
'''
# Creating object from each class
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

'''
# 1. print report. coffee maker and moneymachine has Report method.
coffee_maker.report()
money_machine.report()

#2. Check is resources sufficient
options = menu.get_items()

choice = input(f"What would you like to hace? {options}:  ")
drink = menu.find_drink(choice)

print(coffee_maker.is_resource_sufficient(drink))

#3.Process coins and 4 Check transaction successful

print(money_machine.make_payment(drink.cost))

#5. make coffee

coffee_maker.make_coffee(drink)'

'''
# Here is the complete program

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like to have? {options}:  ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
