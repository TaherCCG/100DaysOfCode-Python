year = int(input("What's your year of birth?"))

# if year > 1980 and year < 1994:
#     print("You are a millennial.")
# elif year > 1994:
#     print("You are a Gen Z.")
    
# When you enter the year 1994, the code does not print anything.

# The condition year > 1980 and year < 1994 excludes the year 1994 because it checks if the year is strictly less than 1994.

# Similarly, the condition year > 1994 excludes the year 1994 because it checks if the year is strictly greater than 1994.

# As a result, the code does not match any of the conditions for the year 1994.

# Solution:
# To include the year 1994, you should adjust the conditions to check for year <= 1994 where appropriate.


if year > 1980 and year <= 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")