try:
    age = int(input("How old are you?"))
    # if user typed in a string, it will raise a ValueError.  This will catch the error and print the message below.
except ValueError:
    print("Please enter a valid number.  Please try again.")

    age = int(input("How old are you?"))
    if age > 18:
        # print("You can drive at age {age}.")
        # print statement is not formatted correctly, and not indented
        print(f"You can drive at age {age}.")
    else:
        print("You can't drive at age {age}.")
