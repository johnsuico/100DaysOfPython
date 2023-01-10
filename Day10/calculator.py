import os

clear = lambda: os.system('cls')

def choose_op():
    print('+ - * /')
    return input("Choose an operator: ")

def calc(op, num1, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    else:
        return False

def continue_calc(result):
    answer = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
    if answer == 'y':
        return True
    else:
        return False

def calculator():
    clear()
    print("Welcome to the calculator.")

    num1 = float(input("What's the first number?: "))

    keep_going = True

    while keep_going:
        op = choose_op()
        num2 = float(input("What's the second number: "))
        result = calc(op, num1, num2)
        if not result:
            print("You did not enter in a valid operator.")
            keep_going = False
            break
        
        print(f"{num1} {op} {num2} = {result}")
        keep_going = continue_calc(result)

        if keep_going:
            num1 = result
        else:
            clear()
            calculator()

    calculator()

calculator()