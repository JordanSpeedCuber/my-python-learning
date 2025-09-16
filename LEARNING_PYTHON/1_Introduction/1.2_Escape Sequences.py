
# ESCAPE SEQUENCES
# Using \" to print double quotes inside double quotes
print("Hello \"Python!\"")
print('Hello "Python!"')  # Using " inside single quotes without escape sequence
print("Path: C:\\Jordan\\Python")  # Using \\ to print backslash
print("Message1\n\nMessage2")  # Using \n to print in new line
print("Message1\tMessage2\n")  # Using \t to print a tab space

# PRACTICE TIME
# First way of printing using \n and \t
print("Your Learning Path:\n\t-Python Basics\n\t-DataEngineering\n\t-AI\n\n")

print("""Your Learning Path:
\t-Python Basics
\t-Data Engineering
\t-AI\n\n\n""")  # Second way of printing using triple quotes

# EXAMPLE OF REAL WORLD USE OF FUNCTION: print()

price_shirt = 25.00
price_jeans = 45.50

qty_shirt = 2
qty_jeans = 1

total_shirt = price_shirt * qty_shirt
total_jeans = price_jeans * qty_jeans
subtotal = total_shirt + total_jeans
print("Subtotal:", subtotal)  # Printing subtotal using comma
discount = subtotal * 0.10
print("Discount:", discount)  # Printing discount using comma
final_total = subtotal - discount

print("Final Total:", final_total)  # Printing final total using comma
