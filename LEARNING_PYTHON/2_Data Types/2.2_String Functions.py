"""
File: 2.2_String Functions.py
Author: Jordan Caycho
Description: Examples of Python string built-in functions and methods
Categories covered:
    - Math category (count)
    - Transformations (replace, concatenation, f-string operations)
    - Split and repetition
    - Indexing & slicing
    - Cleaning methods (strip, lstrip, rstrip)
    - Case conversions
    - Searching methods (startswith, endswith, in, find)
    - Validation methods (isalpha, isnumeric)
"""

# Type Built-in Function for STRING CLASS
name = "Jordan"
print(type(name))

age = 27
print(type(age))
# print("Your age is " + age) #This will give an error because you can't concatenate str and int
# Str() converts any value into a string value
print("Your age is: " + str(age))
age = age + 5  # This will work because both values are integers
age = str(age)  # Now age is a string
print(type(age))  # prints <class 'str'>
# age = age + 5 #This will give an error because you can't concatenate str and int
# Python is flexible with data types - But watch out!
# You can change a value's data type, but Python will treat it differently based on its current type
print('=' * 60)


# 1.MATH CATEGORY METHOD

# 1.1 Count()

text = """
Python is easy to learn!
Python is powerful!
Many people love python!
"""

# count(substracting value) - counts how many times a value appears in a string
print(text.count("Python"))
print(text.count("!"))
print(text.count("$"))  # Value not found, returns 0
print('=' * 60)

# 2.TRANSFORMATIONS CATEGORY METHODS

# 2.1 replace()
price = "1256,34"
print(price.replace(",", "."))  # Replaces comma with dot
print(price)
print('=' * 60)

phone = "935/125/927"
print(phone.replace("/", "-"))  # Replaces slash with dash
print('=' * 60)

price2 = "$1,299.99"
# Chain methods are excecuted left to right
# Removes $ and replaces comma with nothing
print(price2.replace("$", "").replace(",", ""))
print('=' * 60)

# 2.2 'string + string'
first_name = "Jordan"
last_name = "Caycho"
last_name = first_name + " " + last_name
print(last_name)
print('=' * 60)

# example
folder = "C:/users/Jordan"
file = "report.csv"

path = folder + "/" + file
print(f"Full Path: {path}")

# Curly brackets within f-print function
print(f"{{THIS IS JUST A TEXT}}")

# operations within the curly brackets in f-print
print(f"The sum of 5 and 7 is: {5 + 7}")
print('=' * 60)

# 2.3 split()
stamp = "2025-11-15"
print(stamp.split("-"))

csv_file = "Jordan;M;1997/11/24;Peru"
print(csv_file.split(";"))
print('=' * 60)

# 2.4 'string * number'
print("ha" * 3)
print("=" * 60)  # Usually used for structuring console output

# 2.5 Indexation and slicing

# 'cat' [0]
text = "Python"
print(f"Original Text:{text}")
print(f"Positive index [0]:{text[0]}")
print(f"Negative index [-6]:{text[-6]}")  # extracting the first character

print(f"Positive index [5]:{text[5]}")
print(f"Negative index [-1]:{text[-1]}")  # extracting the last character
print("=" * 60)

date = "2026-05-20"
# extracting the year
print("The specified year is: " + date[0:4])
print("The specified year is: " + date[:4])

# extracting the month
print("The specified month is: " + date[5:7])

# extracting the day
print("The specified day is: " + date[8:])
print("The specified day is: " + date[-2:])
print("=" * 60)

# 3. CLEANING CATEGORY METHODS

# 3.1 Cleaning white spaces
data = " Engineer".lstrip()  # removes white spaces from the left side
data2 = "Engineer ".rstrip()  # removes white spaces from the right side
data3 = "  Engineer  ".strip()  # removes white spaces from both sides
# doesn't remove white spaces between words
data4 = "  Future Data Engineer   ".strip()
# It removes any character you want from the start to the end
data5 = "###Data Engineer###".strip("#")

print(data)
print(data2)
print(data3)
print(data4)
print(data5)
print("=" * 60)

text = "   Pipelines"
print(f"Original Text:{text}")
print(f"Total characters:{len(text)}")
# detecting unwanted white spaces
print(f"Total characters without white spaces:{len(text.strip())}")
# total unwanted white spaces
print(f"Total white spaces:{len(text) - len(text.strip())}")
print(
    f"Is the original text cleaned from spaces?: {len(text) == len(text.strip())}")
print("=" * 60)

# 3.2 Case Conversions
search = "Email ".lower().strip()
# Best practice: Always trim spaces and lowercase your data!
data = " email".lower().strip()
print(f"Search value:'{search}'")
print(f"Data value:'{data}'")
print(f"Is Search equal to Data?:'{search == data}'")
print("=" * 60)

# 4. SEARCH CATEGORY METHODS
# Check if the phone number is Peruvian
phone = "+51 935-125-927"
print(f"Phone number: {phone}")
print(f"Is the phone from Peru?: {phone.startswith('+51')},")
print("=" * 60)

# Check if the provided email is valid
email = "jordancaycho@gmail.com"
print(f"Email: {email}")
print(f"Is it a valid email?: {"@" in email and email.endswith(".com")}")
print("=" * 60)

# Check if the API URL is valid
url = "https://api.ejemplo.com/v1/usuarios?rol=admin&activo=true"
print(f"API URL: {url}")
print(f"Is it a valid API link?: {"/api" in url}")
print("=" * 60)

# Find() function : returns a starting position of the word in the string
phone_1 = "+51-933-531-981"
phone_2 = "51-933-531-981"
phone_3 = "0051-933-531-981"
print(f"""Phone number 1:{phone_1}
Phone number 2:{phone_2}
Phone number 3:{phone_3}
""")
# find() is great when combined with other methods to add DYNAMICS
print(f"""Phone number 1 without country code:{phone_1[phone_1.find("-")+1:]}
Phone number 2 without country code:{phone_2[phone_2.find("-")+1:]}
Phone number 3 without country code:{phone_3[phone_3.find("-")+1:]}""")
print("=" * 60)

# 6. VALIDATION CATEGORY METHODS
country = "PERU"
print(country.isalpha())

number = "935125927"
print(number.isnumeric())
