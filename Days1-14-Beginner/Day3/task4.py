print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child Ticket $5.")
    elif age <= 18:
        bill = 7
        print("Youth Ticket $7.")
    else:
        bill = 12
        print("Adult Ticket $12.")

    want_photo = input("Do you want a photo taken? Y or N ")
    if want_photo == "Y" or want_photo == "y":
        bill += 3
        print("Photo added to bill.")

    print(f"Your final bill is ${bill}")

else:
    print("Sorry you have to grow taller before you can ride.")
