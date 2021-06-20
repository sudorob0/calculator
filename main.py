#Calculator
from art import logo
print(logo)

#Adding
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#divide
def divide(n1, n2):
  return n1 / n2



calculation = {
"+": add,
"-": subtract,
"*": multiply,
"/": divide}

cal_cont = True

num1 = float(input("What's the first number?: "))
while cal_cont:
  for sym in calculation:
    print(sym)
  symbol = input("Pick an operation from the line above: " )
  num2 = float(input("What's the next number?: "))

  calculation_function = calculation[symbol]
  answer = calculation_function(num1, num2)
  print(f"{num1} {symbol} {num2} = {answer}")
  continue_cal = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start new calculation.:  ")
  if continue_cal == "y":
    num1 = answer
  else:
    print(logo)
    num1 = float(input("What's the first number?: "))
