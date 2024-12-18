import random

# Password Generator version 1

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
for char in range(0, nr_letters):
    password += random.choice(letters)
    password += random.choice(symbols)
    password += random.choice(numbers)

print(f"Generated password v1 :{password}")


# Password Generator version 2

# Constants
UPPER_CASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER_CASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
NUMBERS = "0123456789"
SPECIAL_CHARACTERS = "!@#$%^&*()_+"

# Variables
password = ""

# Generate password
password += random.choice(UPPER_CASE_LETTERS)
password += random.choice(LOWER_CASE_LETTERS)
password += random.choice(NUMBERS)
password += random.choice(SPECIAL_CHARACTERS)

for i in range(4):
    password += random.choice(UPPER_CASE_LETTERS + LOWER_CASE_LETTERS + NUMBERS + SPECIAL_CHARACTERS)
    
password = ''.join(random.sample(password, len(password)))
print(f"Generated password v2: {password}")



