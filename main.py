# Calculator no GUI

import time
import math

print("Calculator")

def addition():
  time.sleep(1)
  number2 = float(input(f"{number1} +  "))
  add = number1 + number2
  print(add)
  
def multiplication():
  number2 = float(input(f"{number1} x  "))
  multi = number1 * number2
  print(multi)
  
def division():
  time.sleep(1)
  number2 = float(input(f"{number1}/ "))
  divide = number1/number2
  print(divide)
  
def subtraction():
  time.sleep(1)
  number2 = float(input(f"{number1} -  "))
  minus = number1 - number2
  print(minus)

def squareroot():
  sqr = math.sqrt(number1)
  print(sqr)


number1 = float(input("> "))
operator1 = input("Input operator [*, /, -, ^, +]: ").lower()

while True:
  if operator1 == "*":
    multiplication()
    break
  elif operator1 == "-":
    subtraction()
    break
  elif operator1 == "/":
    division()
    break
  elif operator1 == "+":
    addition()
    break
  elif operator1 == "^":
    squareroot()
    break
  else: 
    print("Wrong input")
    break
