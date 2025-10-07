import os
from calc_logo import *

def add(first, last):
    """Adding Numbers"""
    return (first+last)


def subtract(first, last):
    """Subtract Numbers"""
    return (first-last)


def multiply(first, last):
    """Multiply Numbers"""
    return (first*last)


def divide(first, last):
    """Return Divided numbers"""
    return (first/last)


def calc() :
    
    print(logo)
    while True:
        try:
            first_number = float(input("what's the first number?: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    operations = {
            "+": add,
            "-": subtract,
            "*": multiply,
            "/": divide
        }

    for key in operations:
        print(key)

    Condition = True
    while Condition:
        choosen_operation = input('Which operation do You Need ?:')
        if choosen_operation not in operations:
            print("Invalid operation! Please choose a valid operation.")
            continue
        choosen_Function = operations[choosen_operation]

        while True:
            try:
                next_number = float(input('What is your next Number?:'))
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        try:
            Result = choosen_Function(first_number, next_number)
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
            continue

        print(f"{first_number} {choosen_operation} {next_number} = {Result} This operation is {choosen_Function.__name__}")

        next_action = input(f"Type 'y' to continue calculating with {Result}, or type 'n' to start a new calculation: ").lower()
        if next_action == 'y':
            first_number = Result
        elif next_action == 'n':
            Condition = False
            os.system('cls' if os.name == 'nt' else 'clear')
            calc()
            return
        else:
            print("Invalid input! Please enter 'y' or 'n'.")

calc()


        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        



























