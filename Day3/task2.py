# Modula


print(10 % 3)

# Modula is a mathematical operator that returns the remainder of the division of the first number by the second number.

# Example:
# 10 % 3 = 1
# 10 divided by 3 is 3 with a remainder of 1. So 10 % 3 returns 1.

# Modula is useful for checking if a number is even or odd. If a number is divisible by 2, the remainder will be 0. If the remainder is 1, the number is odd.

number = int(input("Which number do you want to check? "))
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
    
# Modula can also be used to check if a number is divisible by another number. If the remainder is 0, the number is divisible by the other number.

number = int(input("Which number do you want to check? "))
if number % 7 == 0:
    print("This number is divisible by 7.")
else:
    print("This number is not divisible by 7.")
    

    