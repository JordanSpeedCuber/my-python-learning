"""
======================================================
 File: 2.4_Practice_Time.py
 Author: Jordan Caycho
 Description: Practice exercises with strings, 
              data cleaning, basic encryption,
              user/email generation, random numbers,
              and inventory validation.
======================================================
"""

import random

# PHONE NUMBER CLEANING
number = "+49 (176) 1234567"
print(number.replace("+", "00").replace("(", "").replace(")", "").replace(" ", ""))
# +49 becomes 0049, removes brackets and spaces
print("=" * 60)

# COUNT VOWELS IN A STRING
text = "Welcome to the Python class!"
total_vowels = (
    text.count("a") +
    text.count("e") +
    text.count("i") +
    text.count("o") +
    text.count("u")
)
print(total_vowels)
print("=" * 60)

# CREATE A SLOGAN
product_name = input("Enter the name of your product: ")
product_quality = input("Describe a quality of your product: ")

print("Discover the new features of", product_name,
      "you will be surprised with its", product_quality)
print("=" * 60)

# SIMPLE DATA CLEANING
price = input("Enter the price in dollars: ")
print(price.replace("$", "").replace(".", ""))
print("=" * 60)

# BASIC ENCRYPTION
message = input("Enter a message you want to encrypt: ")
encrypted = message.replace("a", "4").replace("e", "3")
print(f"Hidden message is: {encrypted}")
print("=" * 60)

# EMAIL GENERATOR
name = input("Enter your 'First Name + Middle Name + Last Name': ")
domain = "@speedcubing.com"
split = name.split(" ")
print("=" * 60)

# extracting first and last name
user = (split[0] + (split[2])).lower()
print("Your new email address is: " + user + domain)
print("=" * 60)

# HASHTAG CREATOR
sentence = input("Enter a phrase or title: ").title()
phrase = sentence.replace(" ", "")
print(f"Hashtag: #{phrase}")
print("=" * 60)

# STRING CLEANING
data = "968-Maria, ( D@t@ Engineer );; 27y  "
print(f"Original Data: {data}")
fmt = (
    data.replace(",", "")
        .replace(";", "")
        .replace("-", " ")
        .replace("@", "a")
        .replace("(", "")
        .replace(")", "")
        .replace("y", "")
        .lower()
        .split()
)
print(f"Convert data to name | role | age")
print(
    f"Generated data! ===> name: {fmt[1]} | role: {fmt[2]} {fmt[3]} | age: {fmt[4]}"
)
print("=" * 60)

# SUBTITLE LOCATOR
video_file = "\"My-journey-through-the-caribbean.mp4.srt\""
print("STRING!:")
print(video_file)
print("Exercise: Indicate the index position of the .mp4 and .srt file extensions")
print(
    f"The index position of .mp4 is: {video_file.find('.mp4')}"
)
print(
    f"The index position of .srt is: {video_file.find('.srt')}"
)
print("=" * 60)

# USERNAME CREATOR
user = input("Please enter your First and Last name: ").strip()
user_final = user.lower()
print(user)
print(f"Contains white spaces: {' ' in user}")
print(f"The space is at index position: {user.find(' ')}")
print(
    f"Generated username: {user_final[0] + user_final[user_final.find(' ') + 1:]}"
)
print("=" * 60)

# RANDOM NUMBER
number = random.randint(1, 100)
print(f'Random number: {number}')
print(f"Is the number even?: {number % 2 == 0}")
print("=" * 60)

# INVENTORY VALIDATOR
value = 'product-ID: 123456789 | stock: 25 | discount: 15%'
print(f'Input value: {value.strip()}')
print(f"The index position of 'stock' is: {value.find('sto')}")
print(f"The index position of 'discount' is: {value.find('disc')}")
final = (
    value.replace("product-ID: ", "")
         .replace("|", "")
         .replace(":", "")
         .replace("%", "")
         .strip()
         .split()
)
stock = int(final[2])
disc = float(final[4])
disc_applied = (100 - disc) / 100
print(f"Number of units in stock: {stock}")
print(f"Total discount: {disc}%")
print(f"The final price of a $1000 product is: ${1000 * disc_applied}")
