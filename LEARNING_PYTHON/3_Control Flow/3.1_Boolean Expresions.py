"""
======================================================
 File: 3.1_Boolean_Expressions.py
 Author: Jordan Caycho
 Description: Examples of boolean expressions, 
              logical operators, and multiple conditions.
======================================================
"""

# 1. BOOLEAN EXPRESSIONS

# 1.1 bool(): Returns True if the value is non-empty or non-zero, 
# returns False if the value is empty, zero, or None
print(bool(1234))
print(bool("Hi"))
print(True)
print(False)
print(type(True))
print(bool())
print(bool(0))
print(bool(""))
print(bool(None))
print("=" * 60)

# 1.2 all() AND any()
# Allows registration if any field is filled
email = 'jordancaycho@gmail.com'
phone = '+51935125927'
username = 'jordanspeedcuber'
print(any([email, phone, username]))  # True if any value is non-empty
# Allows registration only if all fields are filled
print(all([email, phone, username]))
print("=" * 60)

# 1.3 LOGICAL OPERATORS
print(3 > 1 and 5 < 1)  # False
print(3 > 1 and 5 > 1)  # True

print(3 > 1 or 5 < 1)   # True
print(3 < 1 or 5 < 1)   # False
print("=" * 60)

# Check if the system is under critical pressure
cpu_usage = 36
memory_usage = 95
print(f"Is the system critical?: {cpu_usage > 90 or memory_usage > 90}")

# Checking user credentials before login
email_filled = True
password_filled = True
print(f"Is any field missing?: {not (email_filled and password_filled)}")

# not operator flips the boolean value
name = ''
print(not name)
x = 5 > 7
print(not x)

# Multiple conditions
# Allow access only if the user is logged in
# OR if they are a guest
# AND they must NOT be banned
is_logged_in = True
is_guest = False
is_banned = True

print(f"Has access?: {(is_logged_in or is_guest) and not is_banned}")
