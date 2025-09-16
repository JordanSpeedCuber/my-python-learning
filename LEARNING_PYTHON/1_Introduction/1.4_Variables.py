
# Using String Variables
print("My name is Jordan")
print("Jordan is learning Python")
print("Jordan wants to become a Data Engineer\n")

# Assigning string value to variable... variables make updates super easy. One change updates everything
name = "Mike"
print("My name is", name)
print(name, "is learning Python")
# Using comma to print variable depending on position
print(name, "wants to become a Data Engineer\n")

# Python executes code from top to bottom. So changing the variable value here will update all below
name = "Chris"
print("My name is", name)
print(name, "is learning Python")
print(name, "wants to become a Data Engineer\n\n\n")

# PRACTICE TIME
String = "datawithbaraa.com"
print("info@"+String)
print("support@"+String)
print("www."+String, "\n\n\n")

# SIMPLE CONCATENATION
city = "Lima"
country = "Peru"
print("I live in " + city + ", " + country, "\n\n")

# AUTOMATIC EMAIL SIGNATUREsettings
name = "Jordan"
role = "Data Engineer Student"
print("Best regards,\n" + name + "\n" + role, "\n\n")

# USE OF F STRINGS
name = "Jordan"
role = "Future Data Engineer"
website = "jordan.dev"
print(f"""
------------------------------
Name : {name}
Role : {role}
Website : {website}
------------------------------
""")

# Testing strings and {}

name = "Jordan"
age = 27

# print("My name is " +name " and I am " +age) #This will give error because age is integer and cannot be concatenated with string

# This will work because f strings can handle different data types
print(f"My name is {name} and I am {age} years old")
