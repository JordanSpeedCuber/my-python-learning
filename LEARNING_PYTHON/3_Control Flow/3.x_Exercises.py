"""
======================================================
 File: 3.x_Exercises.py
 Author: Jordan Caycho
 Description: Boolean and control flow exercises
              including user validations and role checks.
======================================================
"""

# CHECK IF A USER'S NAME IS NOT EMPTY AND THE AGE IS >= 18
username = input("Enter your username: ")
age = int(input("Enter your age: "))

is_not_empty = bool(username)
age_requirement = age >= 18

print(f"Meets both requirements?: {is_not_empty and age_requirement}")
print("=" * 60)

# CHECK IF THE PASSWORD IS AT LEAST 8 CHARACTERS AND CONTAINS NO SPACES
password = input("Enter your password: ")
print(f"Meets both requirements?: {len(password) >= 8 and ' ' not in password}")
print("=" * 60)

# CHECK IF EMAIL IS NOT EMPTY, CONTAINS '@', AND ENDS WITH '.com'
email = input("Enter your email: ")
is_not_empty = bool(email)
contains_at = '@' in email
ends_with_com = email.endswith(".com")

print(f"Meets all 3 requirements?: {is_not_empty and contains_at and ends_with_com}")
print("=" * 60)

# CHECK IF USERNAME IS A STRING, NOT NONE, AND LONGER THAN 5 CHARACTERS
username = input("Enter your username: ")
is_string = isinstance(username, str)
is_not_none = username is not None
is_long_enough = len(username) > 5

print(f"Meets all 3 requirements?: {is_string and is_not_none and is_long_enough}")
print("=" * 60)

# CHECK USER ROLE AND STATUS
role = input("Enter your role [admin|moderator|user]: ").lower().title().strip()
is_admin = role == 'Admin'
is_moderator = role == 'Moderator'
is_banned = bool(int(input("Is the user banned? (0: No, 1: Yes): ")))
is_email_verified = bool(int(input("Is the email verified? (0: No, 1: Yes): ")))

print(f"Is admin?: {is_admin}")
print(f"Is moderator?: {is_moderator}")
print(f"Is banned?: {is_banned}")
print(f"Is email verified?: {is_email_verified}")
print(f"Meets requirements?: {(is_admin or is_moderator) and (not is_banned or is_email_verified)}")
print("=" * 60)

# CHECK IF A STUDENT CAN ENROLL
# Must be either a member or have paid fees, 
# and either have good grades or be on scholarship
is_member = bool(int(input("Do you have membership? (0: No, 1: Yes): ")))
paid_fees = bool(int(input("Have you paid fees? (0: No, 1: Yes): ")))
has_good_grades = bool(int(input("Do you have good grades? (0: No, 1: Yes): ")))
on_scholarship = bool(int(input("Are you on a scholarship? (0: No, 1: Yes): ")))

can_enroll = (is_member or paid_fees) and (has_good_grades or on_scholarship)
print(f"Can enroll?: {can_enroll}")
print("=" * 60)

# FUTURE EXERCISES PLACEHOLDER:
# - CHECK IF A USER CAN POST: must be verified AND not suspended, OR be a VIP member
# - CHECK IF AN ORDER IS VALID: customer must have account AND sufficient balance, OR have approved credit
# - CHECK IF EMPLOYEE CAN ACCESS: must be full-time OR contractor, AND either not on leave OR have manager approval
# - CHECK IF EVENT CAN START: must have minimum attendees AND venue confirmed, OR be emergency meeting with admin present
