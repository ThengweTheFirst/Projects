# 1 st gen

import random

# The characters that are to be used when generating a password

# Letters
lowercase_letters = "abcdefghijklmnopsrtquvwxyz"
uppercase_letters = lowercase_letters.upper()

# Digits
numbers = "0123456789"

# Signs 
symbols = "~!@#$%^&*()_+{};''\<>,./-"

upper, lower, digits, sym = True, True, True, True

password = ""

if upper:
    password += uppercase_letters
if lower:
    password += lowercase_letters
if digits:
    password += numbers
if sym:
    password += symbols

# To determine the how long the password should be . 
length = 10
amount = 2

# For the final or the end product to be visible on the terminal .
for n in range(amount):
    final_output = "".join(random.sample(password, length))
    print(final_output)
