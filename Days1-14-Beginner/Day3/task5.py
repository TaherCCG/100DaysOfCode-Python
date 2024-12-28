print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

# Set base price for each pizza size
if size == 'S' or size == 's':
    bill = 15
elif size == 'M' or size == 'm':
    bill = 20
elif size == 'L' or size == 'l':
    bill = 25
else:
    print("Invalid pizza size. Please enter S, M or L.")

# Add pepperoni cost based on pizza size
if pepperoni == 'Y' or pepperoni == 'y':
    if size == 'S':
        bill += 2
    else:
        bill += 3

# Add extra cheese cost
if extra_cheese == 'Y' or extra_cheese == 'y':
    bill += 1

# Output the final bill
print(f"Your final bill is: ${bill}")
