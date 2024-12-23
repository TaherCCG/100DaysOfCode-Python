#  Leap year checker

def is_leap_year(year):
    """ Check if the year is a leap year or not."""
    # Write your code here. 
    # Don't change the function name.
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # Check if the year is divisible by 100
        if year % 100 ==0:
            # Check if the year is divisible by 400
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Call function with values
print(is_leap_year(2400))
print(is_leap_year(1989))
print(is_leap_year(1978))
print(is_leap_year(2000))