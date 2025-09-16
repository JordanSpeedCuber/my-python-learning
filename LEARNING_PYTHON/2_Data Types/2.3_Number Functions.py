"""
======================================================
 File: 2.3_Number_Functions.py
 Author: Jordan Caycho
 Description: Examples of Python number functions, 
              conversions, math operators, rounding, 
              random numbers, and validations.
======================================================
"""


# Type Built-in Function for NUMERIC CLASS
import random
import math
num = 5
num1 = 3.5
num2 = 4 + 6j
print(f'Num1: {num}')
print(f'Num2: {num1}')
print(f'Num3: {num2}')
print(f"Type of Num1: {type(num)}")
print(f"Type of Num2: {type(num1)}")
print(f"Type of Num3: {type(num2)}")
print("=" * 60)

# CONVERTING STRING TO INT
x = '24'
print(f"String value: {x}")
print(f"String multiplied by 3: {x * 3}")
x = int(x)
print(f"String converted to INT: {x}")
print(f"INT multiplied by 3: {x * 3}")
print("=" * 60)

# CONVERTING FLOAT TO INT
x = 5.34
print(f"Float value: '{x}'")
x = int(x)
print(f"Float converted to INT: {x}")
print("=" * 60)

# CONVERTING INT TO FLOAT
x = 10
print(f"INT value: '{x}'")
x = float(x)
print(f"INT converted to FLOAT: {x}")
print("=" * 60)

# 1. MATH OPERATORS
print(2 + 3)  # simple addition
print(9 - 5)  # simple subtraction
print(4 * 4)  # simple multiplication
print(7 / 2)  # simple division
print(7 // 2)  # '//' FLOOR DIVISION: divides two numbers and rounds down
# '%' MODULUS (output: 0 or 1) - the remainder, useful to check if a number is even
print(7 % 2)
print(2 ** 3)  # exponentiation: raises a number to the power of another
print("=" * 60)

# 1.1 SHORTCUT OPERATORS
x = 2
x = x + 3
print(x)
y = 6
y += 8
print(y)
y -= 1
print(y)
x *= 6
print(x)
x /= 3
print(x)
print("=" * 60)

# 2. ROUNDING

# Measure distance
print(abs(2 - 10))  # abs() returns the absolute (non-negative) value of a number
print("=" * 60)

# Reducing Numbers
price = 25.54837432234
print(round(price))       # round() rounds up or down depending on the decimal
print(math.floor(price))  # math.floor() rounds the number down
print(math.ceil(price))   # math.ceil() rounds the number up
print(round(price, 2))    # round(x, 2) rounds x to 2 decimal places
print(math.trunc(price))  # math.trunc() removes the decimal part
print("=" * 60)

# Random Module
print(random.random())        # generates a random float between 0 and 1
print(random.randint(1, 100))  # generates a random integer between 1 and 100
print("=" * 60)

# Validation
number = 24.0
print(number.is_integer())   # checks if the float is actually an integer

number2 = 24.7
print(number2.is_integer())  # will return False

x = 70
print(isinstance(x, int))    # checks if x is an integer

y = 70.43
print(isinstance(y, int))    # False
print(isinstance(y, str))    # False
print(isinstance(y, float))  # True
