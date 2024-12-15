# Type Error Checking and conversion

# Type Error
# Fix the len() function so it has no more warnings or errors.
# len(12345)
print(len(str(12345)))


# Type Checking
print(type("12345"))

print(type(12345))

print(type(12345.67))

print(type(True))

print(type(False))

print(type(None))

# Type Conversion
print(str(12345))
print(int("12345"))
print(float("12345.67"))
print(bool("True"))
print(bool("False"))
print(bool(""))

# Make this line of code run without errors
# print("Number of letters in your name: " + len(input("Enter your name")))

print("Number of letters in your name: " + str(len(input("Enter your name: "))))
