import calc_art

def add(a,b):
    return a + b

def sub(a, b):
    return a - b

def div(a, b):
    return a / b

def mul(a, b):
    return a * b


operations = {"+": add,"-": sub, "/": div, "*": mul}

def calculator():
    spacer = " "*5
    for a,b in zip(calc_art.calc.splitlines(),calc_art.calc_letter.splitlines()):
        print(f"{a}{spacer}{b}")
    print("\n"*3)
    should_continue = True
    num1 = float(input("Enter the first number: "))

    while should_continue:
        for sym in operations:
            print(sym)
        operations_symbol = input("Enter the operation symbol you want perform: ")
        num2 = float(input("Enter the second number: "))
        answer = operations[operations_symbol](num1, num2)

        print(f"{num1} {operations_symbol} {num2} is {answer}")

        choice = input(f"Type 'y' if you want to perform another operation with {answer}, type 'n' if you start new calculation \n")

        if choice == 'y':
            num1 = answer
        else:
            should_continue = False
            print("\n" * 10)
            calculator()

calculator()

