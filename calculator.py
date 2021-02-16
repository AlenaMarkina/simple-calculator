# python 3
# calculator.py - simple calculator program


import pyinputplus as pyip

# Asks user to enter two numbers and ensures the user enters a number
number1 = pyip.inputNum(prompt='Please enter number 1: ')
number2 = pyip.inputNum(prompt='Please enter number 2: ')

# Asks user to make choice
result = pyip.inputChoice(['+', '-', '*', '/'])

if result == '+':
    print(number1 + number2)
if result == '-':
    print(number1 - number2)
if result == '*':
    print(number1 * number2)
if result == '/':
    while number2 == 0:
        number2 = pyip.inputNum(prompt='Dividing by 0!\nPlease enter number 2: ')
    print(number1 / number2)
