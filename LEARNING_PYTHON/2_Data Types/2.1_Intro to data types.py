
# Data types
a = 10  # Integer
b = 3.14  # Float
c = "Hello, Python!"  # String
d = 'Hi there!'  # String
e = "1234"  # String
f = True  # Boolean case sensitive
g = False  # Boolean case sensitive
h = None  # NoneType case sensitive
i = ""  # Blank "" is a string value with no characters. its not the same as NoneType
j = " "  # String with a single space character


# Built-in functions
text = "Hello there!"
number = 50

print(type(text))
print(type(number), "\n")

# Len() only works with strings, lists, tuples, dictionaries, etc.
print(len(text), "\n")

# Method of the data type classes
# upper() is a method of string class that converts all characters to uppercase
print(text.upper())
# bit_length() is a method of integer class that returns the number of bits required to represent the integer in binary
print(number.bit_length(), "\n")

# PRACTICE TIME
age = 27
height = 1.78
name = "Jordan"
student = True
graduation = None

# Printing values
print("My name is", name)
print("I am", age, "years old")
print("My height is", height, "meters")
print("Am I a student?", student)
print("Graduation year:", graduation, "\n")

# Printing data types
print(type(age))
print(type(height))
print(type(name))
print(type(student))
print(type(graduation), "\n")

# Printing lenghts of all variables that support len() function
print(len(name))
