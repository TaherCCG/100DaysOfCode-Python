# Prime Number Checker

def is_prime(number):
    """Check if the number is a prime number."""
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Example Input 1
print(is_prime(73))  # Output: True

# Example Input 2
print(is_prime(75))  # Output: False
