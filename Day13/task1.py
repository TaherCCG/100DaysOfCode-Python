def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
# - The for loop iterates through numbers starting from 1 up to, but not including, 20.

# 2. When is the function meant to print "You got it"?
# - The function is meant to print "You got it" when the variable i equals 20.

# 3. What are your assumptions about the value of i?
# - The assumption might be that the value of i will reach 20 during the loop.
#   However, because the range function does not include the end value (20),
#   i will only go up to 19. Therefore, the function will never print "You got it".
#   it needs to be 21 so it goes upto 20

def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")

my_function()
