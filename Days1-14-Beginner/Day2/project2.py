# Project 2: Tip Calculator
# Instructions:
# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay:
# (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? £"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

total_bill = bill + bill * tip / 100
tip_amount = total_bill - bill
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print("\n ===================== \n")
print("Calculating the bill...")
print(f"The bill is £{bill}")
print(f"The tip is {tip}% of the bill, which is £{tip_amount}")
print(f"The total bill is £{total_bill}")
print(f"Number of people the bill was split: {people}")
print(f"Each person should pay: £{final_amount}")
