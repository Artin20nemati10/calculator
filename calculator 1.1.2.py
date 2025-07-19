from colorama import Fore, Style
import math

class Calculator:
    def __init__(self, x, y=None):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def divide(self):
        if self.y == 0:
            return "Error: cannot divide by zero."
        return self.x / self.y

    def power(self):
        return self.x ** self.y

    def sqrt(self):
        if self.x < 0:
            return "Error: cannot take square root of negative number."
        return math.sqrt(self.x)


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(Fore.RED + "Please enter a valid number." + Style.RESET_ALL)


def get_action():
    valid_actions = ['+', '-', '*', '/', '**', 'sqrt', 'q']
    while True:
        action = input("Enter action (+, -, *, /, **, sqrt) or 'q' to quit: ").strip()
        if action in valid_actions:
            return action
        print(Fore.RED + "Invalid action. Try again." + Style.RESET_ALL)


print(Style.BRIGHT + Fore.CYAN + "Welcome to Artin's calculator (v1.1.2)\n" + Style.RESET_ALL)

while True:
    action = get_action()
    if action == 'q':
        print("Goodbye!")
        break

    num1 = get_number("Enter first number: ")

    if action == 'sqrt':
        calc = Calculator(num1)
        print(f"√{num1} = {calc.sqrt()}")
    else:
        num2 = get_number("Enter second number: ")
        calc = Calculator(num1, num2)

        if action == '+':
            print(f"{num1} + {num2} = {calc.add()}")
        elif action == '-':
            print(f"{num1} - {num2} = {calc.subtract()}")
        elif action == '*':
            print(f"{num1} * {num2} = {calc.multiply()}")
        elif action == '/':
            print(f"{num1} / {num2} = {calc.divide()}")
        elif action == '**':
            print(f"{num1} ** {num2} = {calc.power()}")
