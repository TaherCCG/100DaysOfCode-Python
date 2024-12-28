def odd_or_even(number):
    # if number % 2 = 0:
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."
    
number = int(input("Which number do you want to check? "))
print(odd_or_even(number))

# The error in the code is that the comparison operator in the if statement is incorrect. it should be == instead of =.